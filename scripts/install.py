#!/usr/bin/env python3
"""Interactively install selected Harness Starter Pack assets into a project."""

from __future__ import annotations

import argparse
import ctypes
import os
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
ENGLISH_ROOT = REPOSITORY_ROOT / "en"
PORTUGUESE_ROOT = REPOSITORY_ROOT / "pt-br"
LANGUAGE_ROOTS = {"English": ENGLISH_ROOT, "Português (Brasil)": PORTUGUESE_ROOT}
PACKAGE_ROOT = ENGLISH_ROOT
BACKUP_DIRECTORY = ".harness-starter-backups"


class Console:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    CYAN = "\033[36m"
    BLUE = "\033[34m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RED = "\033[31m"

    def __init__(self, no_color: bool = False) -> None:
        self.terminal = sys.stdin.isatty() and sys.stdout.isatty()
        self.ansi = self.terminal and "TERM" in os.environ and os.environ.get("TERM") != "dumb"
        if self.terminal and os.name == "nt":
            self.ansi = self._enable_windows_vt()
        self.color = not no_color and self._color_supported()
        self.unicode = self._unicode_supported()

    @staticmethod
    def _unicode_supported() -> bool:
        try:
            "✓◆─╭╮╰╯".encode(sys.stdout.encoding or "utf-8")
            return True
        except (LookupError, UnicodeEncodeError):
            return False

    @staticmethod
    def _enable_windows_vt() -> bool:
        if os.name != "nt":
            return True
        try:
            kernel32 = ctypes.windll.kernel32  # type: ignore[attr-defined]
            kernel32.GetStdHandle.argtypes = [ctypes.c_int]
            kernel32.GetStdHandle.restype = ctypes.c_void_p
            kernel32.GetConsoleMode.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]
            kernel32.GetConsoleMode.restype = ctypes.c_int
            kernel32.SetConsoleMode.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
            kernel32.SetConsoleMode.restype = ctypes.c_int
            handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
            mode = ctypes.c_uint32()
            if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                return False
            enable_virtual_terminal_processing = 0x0004
            return bool(
                kernel32.SetConsoleMode(
                    handle, mode.value | enable_virtual_terminal_processing
                )
            )
        except (AttributeError, OSError, ValueError):
            return False

    @classmethod
    def _color_supported(cls) -> bool:
        if "NO_COLOR" in os.environ or os.environ.get("TERM", "") == "dumb":
            return False
        if not sys.stdout.isatty():
            return False
        return cls._enable_windows_vt()

    def paint(self, value: str, *styles: str) -> str:
        if not self.color:
            return value
        return "".join(styles) + value + self.RESET

    def heading(self, title: str, step: int | None = None) -> None:
        bullet = "◆" if self.unicode else "*"
        prefix = f"  {step:02d}  " if step is not None else f"  {bullet}  "
        print(self.paint(f"{prefix}{title}", self.BOLD, self.CYAN))

    def success(self, message: str) -> None:
        marker = "✓" if self.unicode else "[+]"
        print(self.paint(f"  {marker}  {message}", self.GREEN))

    def warning(self, message: str) -> None:
        print(self.paint(f"  !  {message}", self.YELLOW))

    def error(self, message: str) -> None:
        marker = "✗" if self.unicode else "[x]"
        print(self.paint(f"  {marker}  {message}", self.RED))

    def note(self, message: str) -> None:
        print(self.paint(f"      {message}", self.DIM))

    def rule(self) -> None:
        line = "─" if self.unicode else "-"
        print(self.paint("  " + line * 58, self.DIM))


def read_menu_key() -> str:
    """Read one navigation key without requiring a third-party terminal package."""
    if os.name == "nt":
        import msvcrt

        key = msvcrt.getwch()
        if key in {"\x00", "\xe0"}:
            return {"H": "up", "P": "down", "G": "home", "O": "end", "K": "left", "M": "right"}.get(
                msvcrt.getwch(), ""
            )
    else:
        import termios
        import tty

        descriptor = sys.stdin.fileno()
        previous = termios.tcgetattr(descriptor)
        try:
            tty.setraw(descriptor)
            key = sys.stdin.read(1)
            if key == "\x1b":
                import select

                if not select.select([sys.stdin], [], [], 0.05)[0]:
                    return "cancel"
                sequence = sys.stdin.read(2)
                return {"[A": "up", "[B": "down", "[H": "home", "[F": "end", "[D": "left", "[C": "right"}.get(
                    sequence, ""
                )
        finally:
            termios.tcsetattr(descriptor, termios.TCSADRAIN, previous)

    if key in {"\r", "\n"}:
        return "enter"
    if key == " ":
        return "toggle"
    if key.lower() == "a":
        return "all"
    if key.lower() == "q":
        return "cancel"
    if key == "\x03":
        raise KeyboardInterrupt
    return ""


def choose_many_interactively(
    console: Console,
    title: str,
    choices: dict[str, str],
    step: int | None,
    initial_selection: list[str] | None = None,
) -> list[str] | None:
    keys = list(choices)
    selected: set[int] = {
        index for index, key in enumerate(keys) if key in (initial_selection or [])
    }
    cursor = 0
    console.heading(title, step)

    def render(previous_lines: int = 0) -> int:
        if previous_lines:
            print(f"\x1b[{previous_lines}A", end="")
        portuguese = PACKAGE_ROOT == PORTUGUESE_ROOT
        lines = [
            "      ↑/↓ mover   Espaço alternar   A alternar todos   ← voltar   →/Enter continuar   Q cancelar"
            if portuguese
            else "      ↑/↓ move   Space toggle   A toggle all   ← back   →/Enter continue   Q cancel",
            f"      Selecionados: {len(selected)}" if portuguese else f"      Selected: {len(selected)}",
        ]
        for index, label in enumerate(choices.values()):
            pointer = ">" if index == cursor else " "
            checkbox = "[✓]" if index in selected and console.unicode else (
                "[x]" if index in selected else "[ ]"
            )
            pointer = console.paint(pointer, console.BOLD, console.CYAN)
            checkbox_style = console.GREEN if index in selected else console.DIM
            checkbox = console.paint(checkbox, checkbox_style)
            lines.append(f"    {pointer} {checkbox}  {label}  ({keys[index]})")
        for line in lines:
            print("\x1b[2K\r" + line)
        sys.stdout.flush()
        return len(lines)

    line_count = render()
    while True:
        key = read_menu_key()
        if key == "up":
            cursor = (cursor - 1) % len(keys) if keys else 0
        elif key == "down":
            cursor = (cursor + 1) % len(keys) if keys else 0
        elif key == "home":
            cursor = 0
        elif key == "end":
            cursor = max(0, len(keys) - 1)
        elif key == "toggle" and keys:
            selected.symmetric_difference_update({cursor})
        elif key == "all":
            selected = set() if len(selected) == len(keys) else set(range(len(keys)))
        elif key in {"enter", "right"}:
            print()
            return [name for index, name in enumerate(keys) if index in selected]
        elif key == "left":
            print()
            return None
        elif key == "cancel":
            raise KeyboardInterrupt
        line_count = render(line_count)


def choose_one_interactively(
    console: Console,
    title: str,
    choices: list[str],
    step: int | None,
    note: str | None = None,
    allow_back: bool = True,
) -> str | None:
    cursor = 0
    console.heading(title, step)
    if note:
        console.note(note)

    def render(previous_lines: int = 0) -> int:
        if previous_lines:
            print(f"\x1b[{previous_lines}A", end="")
        portuguese = PACKAGE_ROOT == PORTUGUESE_ROOT
        navigation = ("← voltar   " if portuguese else "← back   ") if allow_back else ""
        lines = [
            f"      ↑/↓ mover   {navigation}→/Enter selecionar   Q cancelar"
            if portuguese
            else f"      ↑/↓ move   {navigation}→/Enter select   Q cancel"
        ]
        for index, choice in enumerate(choices):
            pointer = ">" if index == cursor else " "
            pointer = console.paint(pointer, console.BOLD, console.CYAN)
            label = console.paint(choice, console.BOLD if index == cursor else console.RESET)
            lines.append(f"    {pointer}  {label}")
        for line in lines:
            print("\x1b[2K\r" + line)
        sys.stdout.flush()
        return len(lines)

    line_count = render()
    while True:
        key = read_menu_key()
        if key == "up":
            cursor = (cursor - 1) % len(choices)
        elif key == "down":
            cursor = (cursor + 1) % len(choices)
        elif key == "home":
            cursor = 0
        elif key == "end":
            cursor = len(choices) - 1
        elif key in {"enter", "right"}:
            print()
            return choices[cursor]
        elif key == "left":
            if allow_back:
                print()
                return None
        elif key == "cancel":
            raise KeyboardInterrupt
        line_count = render(line_count)


@dataclass(frozen=True)
class PlannedFile:
    source: Path | None
    destination: Path
    label: str
    content: str | None = None


STACKS = {
    "aspnet-core": "ASP.NET Core",
    "react": "React",
    "spring-boot": "Java + Spring Boot",
    "node-express": "Node.js + Express",
    "python-fastapi": "Python + FastAPI",
    "angular": "Angular",
    "aspnet-core-react": "ASP.NET Core + React (same repository)",
    "spring-boot-angular": "Java Spring Boot + Angular (same repository)",
}

STACK_BUNDLES = {
    "aspnet-core-react": ("aspnet-core", "react", "aspnet-core-react"),
    "spring-boot-angular": ("spring-boot", "angular", "spring-boot-angular"),
}

HARNESSES = {
    "codex": "Codex",
    "claude-code": "Claude Code",
    "cursor": "Cursor",
    "opencode": "OpenCode",
}

SKILLS = {
    "accessibility-review": "Accessibility review",
    "browser-visual-validation": "Browser visual validation",
    "dependency-review": "Dependency review",
    "feature-brainstorming": "Feature brainstorming",
    "graphify": "Graphify navigation",
    "graphify-setup": "Graphify setup",
    "hook-authoring": "Hook authoring",
    "security-review": "Security review",
    "shift-left-code-review": "Shift-left code review",
    "threat-modeling": "Threat modeling",
    "ui-design-exploration": "UI design exploration",
}

STACKS_PT = {
    "aspnet-core": "ASP.NET Core",
    "react": "React",
    "spring-boot": "Java + Spring Boot",
    "node-express": "Node.js + Express",
    "python-fastapi": "Python + FastAPI",
    "angular": "Angular",
    "aspnet-core-react": "ASP.NET Core + React (mesmo repositório)",
    "spring-boot-angular": "Java + Spring Boot + Angular (mesmo repositório)",
}

HARNESSES_PT = {
    "codex": "Codex",
    "claude-code": "Claude Code",
    "cursor": "Cursor",
    "opencode": "OpenCode",
}

SKILLS_PT = {
    "accessibility-review": "Revisão de acessibilidade",
    "browser-visual-validation": "Validação visual no navegador",
    "dependency-review": "Revisão de dependências",
    "feature-brainstorming": "Exploração de funcionalidades",
    "graphify": "Navegação com Graphify",
    "graphify-setup": "Configuração do Graphify",
    "hook-authoring": "Criação de hooks",
    "security-review": "Revisão de segurança",
    "shift-left-code-review": "Revisão antecipada de código",
    "threat-modeling": "Modelagem de ameaças",
    "ui-design-exploration": "Exploração de design de interface",
}

DEFAULT_SKILLS = ["graphify", "graphify-setup"]

SKILL_DEPENDENCIES = {
    "browser-visual-validation": {"accessibility-review"},
    "ui-design-exploration": {"accessibility-review", "browser-visual-validation"},
}


def choose_many(
    console: Console,
    title: str,
    choices: dict[str, str],
    step: int | None = None,
    initial_selection: list[str] | None = None,
) -> list[str] | None:
    if console.ansi:
        return choose_many_interactively(console, title, choices, step, initial_selection)

    console.heading(title, step)
    portuguese = PACKAGE_ROOT == PORTUGUESE_ROOT
    for index, (key, label) in enumerate(choices.items(), start=1):
        print(f"      {console.paint(str(index), console.BLUE)}  {label}  {console.paint('[' + key + ']', console.DIM)}")
    print("      0  Nenhum" if portuguese else "      0  None")
    if initial_selection:
        console.note(("Seleção atual: " if portuguese else "Current selection: ") + ", ".join(initial_selection))
    while True:
        answer = input(
            "  Selecione números (separados por vírgula), Enter mantém, B volta ou Q cancela: "
            if portuguese
            else "  Select numbers (comma-separated), Enter to keep, B back, or Q cancel: "
        ).strip()
        if answer.lower() == "b":
            return None
        if answer.lower() == "q":
            raise KeyboardInterrupt
        if not answer:
            return initial_selection or []
        try:
            indexes = [int(value.strip()) for value in answer.split(",")]
        except ValueError:
            console.warning("Digite os números exibidos, separados por vírgula." if portuguese else "Enter the displayed numbers, separated by commas.")
            continue
        if 0 in indexes:
            if len(indexes) == 1:
                return []
            console.warning("Escolha 0 sozinho ou selecione um ou mais itens." if portuguese else "Choose 0 by itself, or select one or more items.")
            continue
        if any(index < 1 or index > len(choices) for index in indexes):
            console.warning("Uma ou mais opções estão fora do intervalo listado." if portuguese else "One or more selections are outside the listed range.")
            continue
        keys = list(choices)
        return list(dict.fromkeys(keys[index - 1] for index in indexes))


def choose_one(
    console: Console,
    title: str,
    choices: list[str],
    step: int | None = None,
    note: str | None = None,
    allow_back: bool = True,
) -> str | None:
    if console.ansi:
        return choose_one_interactively(console, title, choices, step, note, allow_back)

    console.heading(title, step)
    if note:
        console.note(note)
    portuguese = PACKAGE_ROOT == PORTUGUESE_ROOT
    for index, choice in enumerate(choices, start=1):
        print(f"      {console.paint(str(index), console.BLUE)}  {choice}")
    print(
        "      " + ("B  Voltar   " if allow_back else "") + "Q  Cancelar"
        if portuguese
        else "      " + ("B  Back   " if allow_back else "") + "Q  Cancel"
    )
    while True:
        answer = input("  Escolha uma opção: " if portuguese else "  Choose an option: ").strip()
        if answer.lower() == "b":
            if allow_back:
                return None
            console.warning("Esta é a primeira etapa; não há etapa anterior." if portuguese else "This is the first step; there is nowhere to go back to.")
            continue
        if answer.lower() == "q":
            raise KeyboardInterrupt
        try:
            index = int(answer)
        except ValueError:
            index = 0
        if 1 <= index <= len(choices):
            return choices[index - 1]
        console.warning(
            f"Digite um número de 1 a {len(choices)}."
            if portuguese else f"Enter a number from 1 to {len(choices)}."
        )


def ask_yes_no(console: Console, prompt: str, default: bool = False) -> bool:
    suffix = "Y/n" if default else "y/N"
    while True:
        answer = input(f"  {prompt} [{suffix}]: ").strip().lower()
        if not answer:
            return default
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        console.warning("Enter y or n.")


def resolve_directory(value: str) -> Path:
    return Path(value).expanduser().resolve()


def collect_files(source_dir: Path, destination_dir: Path, label: str) -> list[PlannedFile]:
    files: list[PlannedFile] = []
    if not source_dir.is_dir():
        raise FileNotFoundError(f"Starter-pack folder is missing: {source_dir}")
    for source in sorted(source_dir.rglob("*")):
        if source.is_symlink():
            raise ValueError(f"Starter-pack assets must not contain symlinks: {source}")
        if source.is_file():
            files.append(
                PlannedFile(
                    source=source,
                    destination=destination_dir / source.relative_to(source_dir),
                    label=label,
                )
            )
    return files


def add_directory(
    plan: list[PlannedFile], relative_source: str, relative_destination: str, label: str
) -> None:
    plan.extend(
        collect_files(
            PACKAGE_ROOT / relative_source,
            Path(relative_destination),
            label,
        )
    )


def add_harness_skill(
    plan: list[PlannedFile], skill: str, target_root: str, label: str
) -> None:
    entries = collect_files(
        PACKAGE_ROOT / "skills" / skill,
        Path(target_root) / skill,
        label,
    )
    for item in entries:
        content = None
        if item.source is not None and item.source.suffix.lower() == ".md":
            content = item.source.read_text(encoding="utf-8")
            for folder in ("docs", "hooks", "guides"):
                content = content.replace(f"../../{folder}/", f"../../../{folder}/")
        plan.append(
            PlannedFile(
                source=item.source,
                destination=item.destination,
                label=item.label,
                content=content,
            )
        )


def resolve_skill_selection(selected: Iterable[str]) -> list[str]:
    resolved = set(selected)
    changed = True
    while changed:
        changed = False
        for skill in tuple(resolved):
            for dependency in SKILL_DEPENDENCIES.get(skill, set()):
                if dependency not in resolved:
                    resolved.add(dependency)
                    changed = True
    return [name for name in SKILLS if name in resolved]


def resolve_stack_selection(selected: Iterable[str]) -> list[str]:
    resolved: set[str] = set()
    for stack in selected:
        resolved.update(STACK_BUNDLES.get(stack, (stack,)))
    return [name for name in STACKS if name in resolved]


def render_harness_readme(
    selected_stacks: list[str], selected_harnesses: list[str], selected_skills: list[str]
) -> str:
    portuguese = PACKAGE_ROOT == PORTUGUESE_ROOT
    stack_names = {
        "aspnet-core": "ASP.NET Core",
        "react": "React",
        "spring-boot": "Java + Spring Boot",
        "node-express": "Node.js + Express",
        "python-fastapi": "Python + FastAPI",
        "angular": "Angular",
        "aspnet-core-react": "ASP.NET Core + React (mesmo repositório)",
        "spring-boot-angular": "Spring Boot + Angular (mesmo repositório)",
    } if portuguese else STACKS
    template_path = PACKAGE_ROOT / "docs" / "templates" / "harness-readme.md"
    template = template_path.read_text(encoding="utf-8")

    selected_stack_lines = [
        f"- [{stack_names[stack]}](stacks/{stack}/README.md)"
        for stack in selected_stacks
    ] or [
        "- Nenhum perfil de stack foi escolhido. Identifique as tecnologias do repositório e adicione perfis ou documente convenções locais."
        if portuguese else
        "- No technology stack profile was selected. Choose and add one later if useful."
    ]

    stack_setup_lines: list[str] = []
    for stack in selected_stacks:
        profile_root = PACKAGE_ROOT / "stacks" / stack
        supplemental = []
        for agreement in ("architecture", "conventions"):
            source = profile_root / "docs" / "agreements" / f"{agreement}.md"
            if source.is_file():
                supplemental.append(
                (
                    f"[Prompts de {agreement}](stacks/{stack}/docs/agreements/{agreement}.md)"
                    if portuguese else
                    f"[{agreement} prompts](stacks/{stack}/docs/agreements/{agreement}.md)"
                )
                )
        templates = profile_root / "docs" / "templates" / "README.md"
        details = ""
        if templates.is_file():
            details = (
                f" Revise os [templates da stack](stacks/{stack}/docs/templates/README.md) "
                "para orientações específicas de spec e verificação."
                if portuguese else
                f" Review [stack templates](stacks/{stack}/docs/templates/README.md) "
                "for focused specs and verification guidance."
            )
        if supplemental:
            details += (
                (" Prompts complementares: " if portuguese else " Supplemental prompts: ")
                + ", ".join(supplemental)
                + (
                    ". Incorpore as decisões aceitas nos acordos raiz ou vincule documentos de perfil mantidos."
                    if portuguese else
                    ". Incorporate accepted decisions into the root project agreements or link to retained profile documents."
                )
            )
        if portuguese:
            stack_setup_lines.append(
                f"- **{stack_names[stack]}:** revise o README e decida quais recomendações de arquitetura, convenções e qualidade se aplicam.{details}"
            )
        else:
            stack_setup_lines.append(
                f"- **{STACKS[stack]}:** review its README and decide which architecture, "
                f"convention, and quality recommendations apply.{details}"
            )
    if not stack_setup_lines:
        stack_setup_lines.append(
            "- Nenhuma configuração específica de stack foi escolhida. Identifique linguagens/frameworks e adicione perfis ou documente convenções locais."
            if portuguese else
            "- No stack-specific setup was selected. Identify the repository's languages/frameworks and add relevant profiles or document local conventions."
        )

    harness_details = {
        "codex": "[Adaptador do Codex](harnesses/codex/README.md); instruções compartilhadas em AGENTS.md e skills em .agents/skills/.",
        "claude-code": "[Adaptador do Claude Code](harnesses/claude-code/CLAUDE.md), CLAUDE.md na raiz e skills em .claude/skills/.",
        "cursor": "[Regra do Cursor](.cursor/rules/harness-starter.mdc); instruções em AGENTS.md e skills em .agents/skills/. Verifique a descoberta de skills na versão usada.",
        "opencode": "[Exemplo do OpenCode](harnesses/opencode/opencode.example.json), configuração opencode.json na raiz e skills em .agents/skills/.",
    }
    if not portuguese:
        harness_details = {
            "codex": "[Codex adapter](harnesses/codex/README.md); shared instructions are in AGENTS.md, with skills in .agents/skills/.",
            "claude-code": "[Claude Code adapter](harnesses/claude-code/CLAUDE.md), generated root CLAUDE.md, and skills in .claude/skills/.",
            "cursor": "[Cursor rule](.cursor/rules/harness-starter.mdc); shared instructions are in AGENTS.md, with skills in .agents/skills/.",
            "opencode": "[OpenCode example](harnesses/opencode/opencode.example.json), installed root opencode.json, and skills in .agents/skills/.",
        }
    harness_lines = [
        f"- **{HARNESSES[harness]}:** {harness_details[harness]}"
        for harness in HARNESSES
        if harness in selected_harnesses
    ]
    if not harness_lines:
        harness_lines.append(
            "- Nenhum adaptador de harness foi escolhido. AGENTS.md está disponível, mas não há adaptador específico nem pasta de descoberta configurada."
            if portuguese else
            "- No harness adapter was selected. Shared instructions are present, but no harness adapter or skill discovery location was configured."
        )

    if selected_skills:
        skill_lines = []
        for skill in selected_skills:
            discovery_paths = []
            if any(harness in selected_harnesses for harness in ("codex", "cursor", "opencode")):
                discovery_paths.append(f"`.agents/skills/{skill}/`")
            if "claude-code" in selected_harnesses:
                discovery_paths.append(f"`.claude/skills/{skill}/`")
            activation = (
                (("Disponível para descoberta em " if portuguese else "Discoverable in ")
                 + " e ".join(discovery_paths) + ".")
                if discovery_paths
                else (
                    "Somente referência; nenhum harness compatível foi escolhido para descoberta."
                    if portuguese else
                    "Reference only; no compatible harness was selected for discovery."
                )
            )
            skill_lines.append(f"- [`{skill}`](skills/{skill}/SKILL.md) — {activation}")
        skill_section = "\n".join(skill_lines)
    else:
        skill_section = (
            "Nenhum fluxo de skill foi escolhido para ativação. A biblioteca portátil de referência em skills/ continua disponível."
            if portuguese else
            "No skill workflows were selected for activation. The portable reference library under skills/ is still available."
        )

    summary = "\n".join(
        [
            ("- **Arquivos de perfis de stack:** " if portuguese else "- **Stack profile files:** ")
            + (", ".join(f"`{stack}`" for stack in selected_stacks)
               if selected_stacks else ("nenhum selecionado" if portuguese else "none selected")),
            ("- **Adaptadores de harness:** " if portuguese else "- **Harness adapters:** ")
            + (", ".join(HARNESSES[item] for item in HARNESSES if item in selected_harnesses)
               if selected_harnesses else ("nenhum selecionado" if portuguese else "none selected")),
            ("- **Fluxos de skills:** " if portuguese else "- **Skill workflows:** ")
            + (", ".join(f"`{skill}`" for skill in selected_skills)
               if selected_skills else ("nenhuma selecionada" if portuguese else "none selected")),
            (
                "- **Sempre copiados:** instruções raiz, cinco acordos, templates comuns, orientações/exemplos de hooks, guias gerais e biblioteca portátil de skills."
                if portuguese else
                "- **Always copied:** root instructions, all five shared agreements, common templates, hook guidance/examples, general guides, and the portable skill reference library."
            ),
        ]
    )

    replacements = {
        "{{INSTALLATION_SUMMARY}}": summary,
        "{{STACK_PROFILES}}": "\n".join(selected_stack_lines),
        "{{HARNESSES}}": "\n".join(harness_lines),
        "{{SKILLS}}": skill_section,
        "{{STACK_SETUP}}": "\n".join(stack_setup_lines),
    }
    for token, content in replacements.items():
        template = template.replace(token, content)
    return template


def build_plan(
    stacks: list[str], harnesses: list[str], selected_skills: list[str]
) -> tuple[list[PlannedFile], list[str]]:
    plan: list[PlannedFile] = []
    portuguese = PACKAGE_ROOT == PORTUGUESE_ROOT
    labels = {
        "agreements": "Acordos comuns" if portuguese else "Core agreements",
        "templates": "Templates comuns" if portuguese else "Core templates",
        "hooks": "Orientações e exemplos de hooks" if portuguese else "Hook guidance and examples",
        "guides": "Guias gerais" if portuguese else "General guides",
        "skills": "Biblioteca de referência de skills (não ativada automaticamente)"
        if portuguese else "Skill reference library (not automatically enabled)",
        "codex": "Orientações para Codex" if portuguese else "Codex guidance",
        "claude-code": "Orientações para Claude Code" if portuguese else "Claude Code guidance",
        "cursor": "Orientações para Cursor" if portuguese else "Cursor guidance",
        "cursor-rule": "Regra para Cursor" if portuguese else "Cursor rule",
        "opencode": "Orientações para OpenCode" if portuguese else "OpenCode guidance",
        "opencode-config": "Configuração do OpenCode" if portuguese else "OpenCode configuration",
        "harness-readme": "Visão geral da instalação e checklist de configuração"
        if portuguese else "Installation overview and setup checklist",
    }
    add_directory(plan, "docs/agreements", "docs/agreements", labels["agreements"])
    add_directory(plan, "docs/templates", "docs/templates", labels["templates"])
    add_directory(plan, "hooks", "hooks", labels["hooks"])
    add_directory(plan, "guides", "guides", labels["guides"])
    add_directory(plan, "skills", "skills", labels["skills"])
    plan.append(
        PlannedFile(
            PACKAGE_ROOT / "AGENTS.md",
            Path("AGENTS.md"),
            "Instruções compartilhadas para agentes" if portuguese else "Shared agent instructions",
        )
    )

    resolved_stacks = resolve_stack_selection(stacks)
    for stack in resolved_stacks:
        stack_name = STACKS_PT[stack] if portuguese else STACKS[stack]
        add_directory(
            plan,
            f"stacks/{stack}",
            f"stacks/{stack}",
            f"Perfil de stack: {stack_name}" if portuguese else f"{stack_name} profile",
        )

    resolved_skills = resolve_skill_selection(selected_skills)
    for skill in resolved_skills:
        skill_name = SKILLS_PT[skill] if portuguese else SKILLS[skill]
        add_directory(
            plan,
            f"skills/{skill}",
            f"skills/{skill}",
            f"Skill: {skill_name}" if portuguese else f"{skill_name} source",
        )

    for harness in harnesses:
        if harness == "codex":
            add_directory(plan, "harnesses/codex", "harnesses/codex", labels["codex"])
        elif harness == "claude-code":
            add_directory(plan, "harnesses/claude-code", "harnesses/claude-code", labels["claude-code"])
            plan.append(
                PlannedFile(
                    None,
                    Path("CLAUDE.md"),
                    "Claude Code project entry point",
                    content=(
                        ("# Instruções do projeto para Claude Code\n\n" if portuguese else "# Claude Code project instructions\n\n")
                        + ("Leia [AGENTS.md](AGENTS.md) e os arquivos relevantes em " if portuguese else "Read the root [AGENTS.md](AGENTS.md) and the relevant files in ")
                        + "[docs/agreements](docs/agreements/README.md) "
                        + ("como contrato compartilhado do projeto.\n\nAs notas específicas do harness estão em " if portuguese else "as the shared project contract.\n\nHarness-specific setup notes are in ")
                        + "[harnesses/claude-code/CLAUDE.md](harnesses/claude-code/CLAUDE.md). "
                        + ("As skills escolhidas ficam em .claude/skills/; o catálogo de referência fica em skills/.\n" if portuguese else "Selected Claude Code skills are installed under .claude/skills/; the portable reference catalog is under skills/.\n")
                    ),
                )
            )
        elif harness == "cursor":
            add_directory(plan, "harnesses/cursor", "harnesses/cursor", labels["cursor"])
            add_directory(plan, "harnesses/cursor/rules", ".cursor/rules", labels["cursor-rule"])
        elif harness == "opencode":
            add_directory(plan, "harnesses/opencode", "harnesses/opencode", labels["opencode"])
            plan.append(
                PlannedFile(
                    REPOSITORY_ROOT / "opencode.json",
                    Path("opencode.json"),
                    labels["opencode-config"],
                )
            )

    skill_targets: list[tuple[str, str]] = []
    if "codex" in harnesses or "cursor" in harnesses or "opencode" in harnesses:
        skill_targets.append((".agents/skills", "Skills de agente" if portuguese else "Agent skills"))
    if "claude-code" in harnesses:
        skill_targets.append((".claude/skills", "Skills do Claude Code" if portuguese else "Claude Code skills"))
    for skill in resolved_skills:
        for target_root, label in skill_targets:
            skill_name = SKILLS_PT[skill] if portuguese else SKILLS[skill]
            add_harness_skill(plan, skill, target_root, f"{label}: {skill_name}")

    plan.append(
        PlannedFile(
            source=None,
            destination=Path("HARNESS-README.md"),
            label=labels["harness-readme"],
            content=render_harness_readme(resolved_stacks, harnesses, resolved_skills),
        )
    )

    unique: dict[Path, PlannedFile] = {}
    for item in plan:
        previous = unique.get(item.destination)
        if previous and previous.source != item.source:
            raise ValueError(f"Two selected assets target the same file: {item.destination}")
        unique[item.destination] = item
    return list(unique.values()), resolved_skills


def safe_destination(target_root: Path, relative_path: Path) -> Path:
    if relative_path.is_absolute() or ".." in relative_path.parts:
        raise ValueError(f"Unsafe destination path in starter pack: {relative_path}")
    destination = target_root / relative_path
    resolved_parent = destination.parent.resolve()
    try:
        resolved_parent.relative_to(target_root)
    except ValueError as error:
        raise ValueError(f"Destination resolves outside the target folder: {destination}") from error
    return destination


def make_plan(target_root: Path, files: list[PlannedFile]) -> list[tuple[PlannedFile, Path]]:
    return [(item, safe_destination(target_root, item.destination)) for item in files]


def show_plan(console: Console, target: Path, files: list[tuple[PlannedFile, Path]]) -> None:
    portuguese = PACKAGE_ROOT == PORTUGUESE_ROOT
    console.heading("Revise a instalação" if portuguese else "Review installation", 6)
    print(f"      {'Destino' if portuguese else 'Destination'}: {target}")
    print(f"      {'Arquivos' if portuguese else 'Files'}: {len(files)}")
    console.rule()
    previous_label = None
    for item, destination in files:
        if item.label != previous_label:
            print(console.paint(f"  {item.label}", console.BOLD))
            previous_label = item.label
        state = (
            ("perguntará sobre substituição" if portuguese else "replace prompt")
            if destination.exists() or destination.is_symlink()
            else ("novo" if portuguese else "new")
        )
        color = console.YELLOW if state == "replace prompt" else console.GREEN
        print(f"      {console.paint(state, color)}  {item.destination.as_posix()}")
    console.rule()


def backup_path(target: Path) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    candidate = target / BACKUP_DIRECTORY / timestamp
    suffix = 1
    while candidate.exists():
        candidate = target / BACKUP_DIRECTORY / f"{timestamp}-{suffix}"
        suffix += 1
    return candidate


def apply_plan(
    console: Console,
    target: Path,
    files: list[tuple[PlannedFile, Path]],
) -> tuple[int, int, list[Path], list[str]]:
    decisions: dict[Path, bool] = {}
    for item, destination in files:
        if destination.exists() or destination.is_symlink():
            portuguese = PACKAGE_ROOT == PORTUGUESE_ROOT
            if destination.is_symlink():
                collision_type = "Link simbólico existente" if portuguese else "Existing symbolic link"
            elif destination.is_dir():
                collision_type = (
                    "Diretório existente (todo o conteúdo será incluído no backup)"
                    if portuguese else "Existing directory (all contents will be backed up together)"
                )
            else:
                collision_type = "Arquivo existente" if portuguese else "Existing file"
            console.warning(f"{collision_type}: {item.destination.as_posix()}")
            replace = ask_yes_no(
                console,
                "Fazer backup deste item e substituí-lo?" if portuguese else "Back up this item, then replace it?",
                default=False,
            )
            decisions[destination] = replace

    accepted = [
        (item, destination)
        for item, destination in files
        if not (destination.exists() or destination.is_symlink()) or decisions.get(destination, False)
    ]
    skipped = len(files) - len(accepted)
    backup_root = backup_path(target) if any(decisions.values()) else None
    installed = 0
    failures: list[str] = []
    backups: list[Path] = []

    try:
        target.mkdir(parents=True, exist_ok=True)
        if backup_root is not None:
            backup_relative = backup_root.relative_to(target)
            safe_destination(target, backup_relative)
            backup_root.mkdir(parents=True, exist_ok=False)
            safe_destination(target, backup_relative)
        for item, destination in accepted:
            try:
                safe_destination(target, item.destination)
                if destination.exists() or destination.is_symlink():
                    if not decisions.get(destination, False):
                        continue
                    assert backup_root is not None
                    backup = backup_root / item.destination
                    backup.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(destination, backup)
                    backups.append(backup)
                destination.parent.mkdir(parents=True, exist_ok=True)
                if item.content is not None:
                    with destination.open("w", encoding="utf-8", newline="\n") as output:
                        output.write(item.content)
                elif item.source is not None:
                    shutil.copy2(item.source, destination)
                else:
                    raise ValueError(f"No content source was defined for {item.destination}")
                installed += 1
                marker = "✓" if console.unicode else "[+]"
                print(f"  {console.paint(marker, console.GREEN)}  {item.destination.as_posix()}")
            except (OSError, ValueError) as error:
                failures.append(f"{item.destination.as_posix()}: {error}")
                console.error(
                    f"Não foi possível instalar {item.destination.as_posix()}: {error}"
                    if PACKAGE_ROOT == PORTUGUESE_ROOT
                    else f"Could not install {item.destination.as_posix()}: {error}"
                )
    except OSError as error:
        failures.append(f"Destination: {error}")
        console.error(
            f"Não foi possível preparar o destino: {error}"
            if PACKAGE_ROOT == PORTUGUESE_ROOT
            else f"Could not prepare destination: {error}"
        )

    return installed, skipped, backups, failures


def make_target(
    console: Console, mode: str, current_target: Path | None = None
) -> Path | None:
    is_new = mode == "New project folder"
    while True:
        prompt = "Path for the new project folder: " if is_new else "Path to the existing repository: "
        if current_target:
            prompt = f"{prompt}[Enter keeps {current_target}, B goes back]: "
        else:
            prompt = f"{prompt}[B goes back]: "
        value = input(f"  {prompt}").strip().strip('"')
        if value.lower() == "b":
            return None
        if not value:
            if current_target is None:
                console.warning("A destination path is required before continuing.")
                continue
            target = current_target
        else:
            target = resolve_directory(value)
        if is_new and target.exists():
            console.warning("That path already exists. Choose a new folder path or use existing repository mode.")
            continue
        if not is_new and not target.is_dir():
            console.warning("That path is not an existing directory.")
            continue
        try:
            target.relative_to(REPOSITORY_ROOT)
        except ValueError:
            return target
        console.error("The destination cannot be this starter-pack repository or a folder inside it.")


def print_banner(console: Console) -> None:
    print()
    if console.unicode:
        top = "  ╭──────────────────────────────────────────────────────────╮"
        title = "  │  ◆  Harness Starter Pack                                  │"
        subtitle = "  │     Configure reusable AI engineering guidance            │"
        bottom = "  ╰──────────────────────────────────────────────────────────╯"
    else:
        top = "  +----------------------------------------------------------+"
        title = "  |  *  Harness Starter Pack                                  |"
        subtitle = "  |     Configure reusable AI engineering guidance            |"
        bottom = "  +----------------------------------------------------------+"
    print(console.paint(top, console.CYAN))
    print(console.paint(title, console.BOLD, console.CYAN))
    print(console.paint(subtitle, console.DIM))
    print(console.paint(bottom, console.CYAN))
    print()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install selected Harness Starter Pack guidance into a project."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="show the selected file plan without creating or changing files",
    )
    parser.add_argument("--no-color", action="store_true", help="disable colored console output")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    global PACKAGE_ROOT
    PACKAGE_ROOT = ENGLISH_ROOT
    args = parse_args(sys.argv[1:] if argv is None else argv)
    console = Console(no_color=args.no_color)
    try:
        print_banner(console)
        console.note("English / Português (Brasil) - Python standard library - Windows / macOS / Linux")
        console.note("The wizard copies guidance only; it does not install application dependencies or global harness settings.")
        print()

        mode: str | None = None
        target: Path | None = None
        stacks: list[str] = []
        harnesses: list[str] = []
        skills = DEFAULT_SKILLS.copy()
        step = 0
        prepared: list[tuple[PlannedFile, Path]] = []
        while True:
            if step == 0:
                selected_mode = choose_one(
                    console,
                    "Onde instalar os arquivos? / Where should the starter files go?",
                    ["Nova pasta de projeto", "Repositório existente"],
                    1,
                    allow_back=False,
                )
                if selected_mode is not None:
                    mode = selected_mode
                    step = 1
            elif step == 1:
                assert mode is not None
                mode_for_path = "New project folder" if mode == "Nova pasta de projeto" else mode
                selected_target = make_target(console, mode_for_path, target)
                if selected_target is None:
                    step = 0
                else:
                    target = selected_target
                    step = 2
            elif step == 2:
                language = choose_one(
                    console,
                    "Choose language / Escolha o idioma",
                    list(LANGUAGE_ROOTS),
                    2,
                    note="Select the language of the guidance to install / Selecione o idioma das orientações.",
                )
                if language is None:
                    step = 1
                else:
                    PACKAGE_ROOT = LANGUAGE_ROOTS[language]
                    step = 3
            elif step == 3:
                stack_options = STACKS_PT if PACKAGE_ROOT == PORTUGUESE_ROOT else STACKS
                selected_stacks = choose_many(
                    console,
                    "Escolha os perfis de stack" if PACKAGE_ROOT == PORTUGUESE_ROOT else "Choose stack profiles",
                    stack_options,
                    3,
                    stacks,
                )
                if selected_stacks is None:
                    step = 2
                else:
                    stacks = selected_stacks
                    step = 4
            elif step == 4:
                harness_options = HARNESSES_PT if PACKAGE_ROOT == PORTUGUESE_ROOT else HARNESSES
                selected_harnesses = choose_many(
                    console,
                    "Escolha os harnesses" if PACKAGE_ROOT == PORTUGUESE_ROOT else "Choose harnesses",
                    harness_options,
                    4,
                    harnesses,
                )
                if selected_harnesses is None:
                    step = 3
                else:
                    harnesses = selected_harnesses
                    step = 5
            elif step == 5:
                skill_options = SKILLS_PT if PACKAGE_ROOT == PORTUGUESE_ROOT else SKILLS
                selected_skills = choose_many(
                    console,
                    "Escolha as skills (Graphify e configuração vêm selecionadas)"
                    if PACKAGE_ROOT == PORTUGUESE_ROOT
                    else "Choose skills (Graphify and setup selected by default)",
                    skill_options,
                    5,
                    skills,
                )
                if selected_skills is None:
                    step = 4
                else:
                    skills = selected_skills
                    assert target is not None
                    resolved_skills = resolve_skill_selection(skills)
                    added_dependencies = sorted(set(resolved_skills) - set(skills))
                    if added_dependencies:
                        console.note(
                            ("Skills de apoio necessárias também serão incluídas: "
                             if PACKAGE_ROOT == PORTUGUESE_ROOT
                             else "Required supporting skills will also be included: ")
                            + ", ".join(added_dependencies)
                        )
                    files, _ = build_plan(stacks, harnesses, skills)
                    prepared = make_plan(target, files)
                    show_plan(console, target, prepared)
                    if args.dry_run:
                        console.warning(
                            "Prévia solicitada; nenhum arquivo será gravado."
                            if PACKAGE_ROOT == PORTUGUESE_ROOT
                            else "Dry run requested; nothing will be written."
                        )
                        console.success(
                            "Prévia concluída. Nenhum arquivo ou diretório foi alterado."
                            if PACKAGE_ROOT == PORTUGUESE_ROOT
                            else "Preview complete. No files or directories were changed."
                        )
                        return 0
                    step = 6
            elif step == 6:
                action = choose_one(
                    console,
                    "Revise a próxima etapa" if PACKAGE_ROOT == PORTUGUESE_ROOT else "Review next step",
                    ["Aplicar este plano", "Voltar às skills opcionais", "Cancelar instalação"]
                    if PACKAGE_ROOT == PORTUGUESE_ROOT
                    else ["Apply this file plan", "Back to optional skills", "Cancel installation"],
                    6,
                    note="Use a seta para a esquerda para revisar escolhas anteriores."
                    if PACKAGE_ROOT == PORTUGUESE_ROOT
                    else "Go back with the left arrow to revisit earlier choices.",
                )
                if action is None or action in {"Back to optional skills", "Voltar às skills opcionais"}:
                    step = 5
                elif action in {"Cancel installation", "Cancelar instalação"}:
                    console.warning("Cancelado. O destino não foi alterado." if PACKAGE_ROOT == PORTUGUESE_ROOT else "Cancelled. The destination was not changed.")
                    return 0
                else:
                    break

        assert target is not None and mode is not None
        is_new = mode in {"New project folder", "Nova pasta de projeto"}

        installed, skipped, backups, failures = apply_plan(console, target, prepared)

        initialized_git = False
        if is_new and not args.dry_run and not failures:
            if ask_yes_no(
                console,
                "Inicializar um repositório Git aqui com git init?"
                if PACKAGE_ROOT == PORTUGUESE_ROOT
                else "Initialize a Git repository here with git init?",
                default=False,
            ):
                try:
                    import subprocess

                    subprocess.run(["git", "init", str(target)], check=True)
                    initialized_git = True
                    console.success("Repositório Git inicializado." if PACKAGE_ROOT == PORTUGUESE_ROOT else "Git repository initialized.")
                except Exception as error:
                    failures.append(f"git init: {error}")
                    console.error(
                        f"Não foi possível inicializar o Git: {error}"
                        if PACKAGE_ROOT == PORTUGUESE_ROOT
                        else f"Could not initialize Git: {error}"
                    )

        console.rule()
        if failures:
            console.error(
                f"Concluído com {len(failures)} problema(s). Revise os caminhos acima."
                if PACKAGE_ROOT == PORTUGUESE_ROOT
                else f"Finished with {len(failures)} issue(s). Review the paths above."
            )
        else:
            console.success("Configuração concluída." if PACKAGE_ROOT == PORTUGUESE_ROOT else "Setup complete.")
        print(
            f"      Instalados: {installed}   Ignorados: {skipped}   Problemas: {len(failures)}"
            if PACKAGE_ROOT == PORTUGUESE_ROOT
            else f"      Installed: {installed}   Skipped: {skipped}   Issues: {len(failures)}"
        )
        if backups:
            backup_folder = target / BACKUP_DIRECTORY
            console.note(
                f"Arquivos substituídos foram salvos em: {backup_folder}"
                if PACKAGE_ROOT == PORTUGUESE_ROOT
                else f"Replaced files were backed up under: {backup_folder}"
            )
        if is_new and not initialized_git:
            console.note("Para inicializar o Git depois, execute: git init" if PACKAGE_ROOT == PORTUGUESE_ROOT else "To initialize Git later, run: git init")
        console.note(
            "Próximo passo: revise AGENTS.md e adapte docs/agreements/ ao projeto."
            if PACKAGE_ROOT == PORTUGUESE_ROOT
            else "Next: review AGENTS.md and tailor docs/agreements/ to this project."
        )
        if "claude-code" in harnesses:
            console.note(
                "Claude Code: revise o CLAUDE.md gerado na raiz e .claude/skills/."
                if PACKAGE_ROOT == PORTUGUESE_ROOT
                else "Claude Code: review the generated root CLAUDE.md and .claude/skills/."
            )
        if "cursor" in harnesses:
            console.note(
                "Cursor: revise .cursor/rules/ e .agents/skills/ na versão instalada."
                if PACKAGE_ROOT == PORTUGUESE_ROOT
                else "Cursor: review .cursor/rules/ and .agents/skills/ in your installed version."
            )
        if "opencode" in harnesses:
            console.note(
                "OpenCode: revise opencode.json e mescle preferências de modelo/provedor se necessário."
                if PACKAGE_ROOT == PORTUGUESE_ROOT
                else "OpenCode: review opencode.json and merge your model/provider preferences if needed."
            )
        return 1 if failures else 0
    except (KeyboardInterrupt, EOFError):
        print("\n" + console.paint("  Cancelled.", console.YELLOW))
        return 130
    except (OSError, ValueError) as error:
        console.error(str(error))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
