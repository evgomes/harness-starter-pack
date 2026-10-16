#!/usr/bin/env python3
"""Rebuild and verify a local, code-only Graphify index (Python 3 standard library only)."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".ps1", ".psm1", ".psd1", ".sh", ".bash", ".sln", ".slnx", ".csproj",
    ".fsproj", ".vbproj", ".cs", ".razor", ".cshtml", ".xaml", ".ts", ".tsx",
    ".mts", ".cts", ".js", ".jsx", ".mjs", ".json", ".vue", ".svelte",
    ".astro", ".sql", ".py", ".go", ".rs", ".java", ".kt", ".kts",
    ".scala", ".php", ".rb", ".c", ".h", ".cpp", ".cc", ".cxx", ".hpp",
    ".swift", ".dart",
}
EXCLUDED_FOLDERS = (
    ".claude/", ".agents/", ".codex/", ".cursor/", ".opencode/",
    ".git/", "graphify-out/", "node_modules/", "dist/", "build/", "bin/", "obj/",
)
EXCLUDED_FILE_SUFFIXES = ("package-lock.json",)


def run_git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, text=True, check=False
    )
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(detail or f"git {' '.join(args)} failed ({result.returncode})")
    return result


def repository_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=False
    )
    if result.returncode != 0 or not result.stdout.strip():
        raise RuntimeError("Run this script from inside a Git repository.")
    return Path(result.stdout.strip()).resolve()


def is_excluded(relative_path: str) -> bool:
    path = relative_path.replace("\\", "/").lower()
    if any(path.startswith(folder.lower()) or f"/{folder.lower()}" in path for folder in EXCLUDED_FOLDERS):
        return True
    return any(path.lower().endswith(suffix.lower()) for suffix in EXCLUDED_FILE_SUFFIXES)


def current_code_files(root: Path) -> dict[str, Path]:
    result = run_git(root, "ls-files", "--cached", "--others", "--exclude-standard")
    files: dict[str, Path] = {}
    for raw in result.stdout.splitlines():
        relative = raw.replace("\\", "/")
        if is_excluded(relative) or Path(relative).suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        full_path = (root / raw).resolve()
        if full_path.is_file() and full_path.is_relative_to(root):
            files[relative] = full_path
    return files


def freshness(root: Path, graph_path: Path, manifest_path: Path) -> tuple[bool, str, int]:
    if not graph_path.is_file() or not manifest_path.is_file():
        return False, "graph or manifest is missing", 0

    try:
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return False, f"graph or manifest cannot be read: {error}", 0

    if any(
        node.get("source_file")
        and Path(str(node["source_file"])).suffix.lower() == ".md"
        for node in graph.get("nodes", [])
    ):
        return False, "graph contains Markdown nodes from an unsafe incremental update", 0
    if not isinstance(manifest, dict):
        return False, "manifest has an unexpected format", 0

    indexed = {
        str(name).replace("\\", "/"): value
        for name, value in manifest.items()
        if Path(str(name)).suffix.lower() in SUPPORTED_EXTENSIONS
    }
    for relative, entry in indexed.items():
        full_path = root / relative
        if not full_path.is_file():
            return False, f"indexed file was removed: {relative}", len(indexed)
        expected = str(entry.get("ast_hash", "")) if isinstance(entry, dict) else ""
        actual = hashlib.md5(full_path.read_bytes()).hexdigest()
        if actual.lower() != expected.lower():
            return False, f"source changed: {relative}", len(indexed)

    for relative in current_code_files(root):
        if relative not in indexed:
            return False, f"new source file: {relative}", len(indexed)
    return True, "source hashes match the code-only manifest", len(indexed)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true", help="check index freshness without changes")
    parser.add_argument("--force", action="store_true", help="rebuild even if the index is fresh")
    args = parser.parse_args()

    try:
        root = repository_root()
        output_dir = (root / "graphify-out").resolve()
        if output_dir.parent != root:
            raise RuntimeError(f"Refusing unexpected Graphify output path: {output_dir}")
        graph_path = output_dir / "graph.json"
        manifest_path = output_dir / "manifest.json"
        fresh, reason, count = freshness(root, graph_path, manifest_path)

        if args.check_only:
            state = "fresh" if fresh else "stale"
            print(f"Graphify index is {state}: {reason} ({count} indexed files).")
            return 0 if fresh else 2
        if fresh and not args.force:
            print(f"Graphify index is fresh ({count} indexed files); rebuild skipped.")
            return 0

        tracked = run_git(root, "ls-files", "--", "graphify-out").stdout.strip()
        if tracked:
            raise RuntimeError("Refusing to replace graphify-out because it contains tracked files.")
        ignored = run_git(root, "check-ignore", "-q", "--", "graphify-out/graph.json", check=False)
        if ignored.returncode != 0:
            raise RuntimeError("Refusing to rebuild until graphify-out/ is ignored by Git.")

        if output_dir.is_symlink():
            output_dir.unlink()
        elif output_dir.exists():
            shutil.rmtree(output_dir)

        subprocess.run(
            ["graphify", "extract", ".", "--code-only", "--timing"], cwd=root, check=True
        )
        subprocess.run(
            ["graphify", "diagnose", "multigraph", "--graph", str(graph_path), "--max-examples", "3"],
            cwd=root,
            check=True,
        )
        fresh, reason, count = freshness(root, graph_path, manifest_path)
        if not fresh:
            raise RuntimeError(f"Graphify rebuilt, but its manifest is still stale: {reason}")
        print(f"Graphify index rebuilt and verified ({count} indexed files).")
        return 0
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
