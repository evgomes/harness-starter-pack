#!/usr/bin/env python3
"""Reconstrói e verifica um índice Graphify local somente de código (apenas biblioteca padrão do Python 3)."""
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
        raise RuntimeError("Execute este script de dentro de um repositório Git.")
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
        return False, "o grafo ou o manifesto não existe", 0

    try:
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return False, f"não foi possível ler o grafo ou o manifesto: {error}", 0

    if any(
        node.get("source_file")
        and Path(str(node["source_file"])).suffix.lower() == ".md"
        for node in graph.get("nodes", [])
    ):
        return False, "o grafo contém nós Markdown de uma atualização incremental insegura", 0
    if not isinstance(manifest, dict):
        return False, "o manifesto tem um formato inesperado", 0

    indexed = {
        str(name).replace("\\", "/"): value
        for name, value in manifest.items()
        if Path(str(name)).suffix.lower() in SUPPORTED_EXTENSIONS
    }
    for relative, entry in indexed.items():
        full_path = root / relative
        if not full_path.is_file():
            return False, f"arquivo indexado foi removido: {relative}", len(indexed)
        expected = str(entry.get("ast_hash", "")) if isinstance(entry, dict) else ""
        actual = hashlib.md5(full_path.read_bytes()).hexdigest()
        if actual.lower() != expected.lower():
            return False, f"o código-fonte mudou: {relative}", len(indexed)

    for relative in current_code_files(root):
        if relative not in indexed:
            return False, f"novo arquivo de código-fonte: {relative}", len(indexed)
    return True, "os hashes do código-fonte correspondem ao manifesto somente de código", len(indexed)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true", help="verifica a atualidade do índice sem alterações")
    parser.add_argument("--force", action="store_true", help="reconstrói mesmo se o índice estiver atualizado")
    args = parser.parse_args()

    try:
        root = repository_root()
        output_dir = (root / "graphify-out").resolve()
        if output_dir.parent != root:
            raise RuntimeError(f"Caminho inesperado para a saída do Graphify; operação recusada: {output_dir}")
        graph_path = output_dir / "graph.json"
        manifest_path = output_dir / "manifest.json"
        fresh, reason, count = freshness(root, graph_path, manifest_path)

        if args.check_only:
            state = "atualizado" if fresh else "desatualizado"
            print(f"Índice do Graphify {state}: {reason} ({count} arquivos indexados).")
            return 0 if fresh else 2
        if fresh and not args.force:
            print(f"Índice do Graphify atualizado ({count} arquivos indexados); reconstrução ignorada.")
            return 0

        tracked = run_git(root, "ls-files", "--", "graphify-out").stdout.strip()
        if tracked:
            raise RuntimeError("Recusa em substituir graphify-out porque contém arquivos rastreados pelo Git.")
        ignored = run_git(root, "check-ignore", "-q", "--", "graphify-out/graph.json", check=False)
        if ignored.returncode != 0:
            raise RuntimeError("Recusa em reconstruir até que graphify-out/ seja ignorado pelo Git.")

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
            raise RuntimeError(f"O Graphify foi reconstruído, mas o manifesto continua desatualizado: {reason}")
        print(f"Índice do Graphify reconstruído e verificado ({count} arquivos indexados).")
        return 0
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
