"""Focused checks for the starter pack installer using temporary directories."""

from __future__ import annotations

import io
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts import install
from scripts.install import (
    Console,
    PlannedFile,
    REPOSITORY_ROOT,
    apply_plan,
    build_plan,
    make_plan,
)


class BuildPlanTests(unittest.TestCase):
    def test_selects_stack_harness_and_only_requested_discovery_skills(self) -> None:
        files, resolved_skills = build_plan(
            stacks=["react"],
            harnesses=["cursor"],
            selected_skills=["browser-visual-validation"],
        )
        paths = {file.destination.as_posix(): file for file in files}

        self.assertIn("AGENTS.md", paths)
        self.assertIn("docs/agreements/architecture.md", paths)
        self.assertIn("stacks/react/README.md", paths)
        self.assertIn(".cursor/rules/harness-starter.mdc", paths)
        self.assertIn(".agents/skills/browser-visual-validation/SKILL.md", paths)
        self.assertIn(".agents/skills/accessibility-review/SKILL.md", paths)
        self.assertNotIn(".agents/skills/feature-brainstorming/SKILL.md", paths)
        self.assertIn("accessibility-review", resolved_skills)

        active_skill = paths[".agents/skills/browser-visual-validation/SKILL.md"]
        self.assertIn("../../../guides/browser-testing.md", active_skill.content or "")

    def test_new_claude_entrypoint_is_generated_for_the_target_project(self) -> None:
        files, _ = build_plan([], ["claude-code"], [])
        paths = {file.destination.as_posix(): file for file in files}

        entry = paths["CLAUDE.md"]
        self.assertIsNone(entry.source)
        self.assertIn("docs/agreements/README.md", entry.content or "")
        self.assertIn(".claude/skills/", entry.content or "")


class InteractiveSelectionTests(unittest.TestCase):
    def test_checkbox_menu_supports_selecting_multiple_items(self) -> None:
        console = Console(no_color=True)
        keys = iter(["toggle", "down", "toggle", "enter"])
        output = io.StringIO()

        with (
            patch.object(console, "ansi", True),
            patch("scripts.install.read_menu_key", side_effect=lambda: next(keys)),
            redirect_stdout(output),
        ):
            selected = install.choose_many(console, "Choose profiles", {"dotnet": ".NET", "react": "React"})

        self.assertEqual(selected, ["dotnet", "react"])
        self.assertIn("Space toggle", output.getvalue())

    def test_single_choice_menu_uses_keyboard_navigation(self) -> None:
        console = Console(no_color=True)
        keys = iter(["down", "enter"])
        output = io.StringIO()

        with (
            patch.object(console, "ansi", True),
            patch("scripts.install.read_menu_key", side_effect=lambda: next(keys)),
            redirect_stdout(output),
        ):
            selected = install.choose_one(
                console, "Choose destination", ["New project folder", "Existing repository"]
            )

        self.assertEqual(selected, "Existing repository")
        self.assertIn("Enter select", output.getvalue())

    def test_left_arrow_returns_to_previous_step(self) -> None:
        console = Console(no_color=True)
        with (
            patch.object(console, "ansi", True),
            patch("scripts.install.read_menu_key", return_value="left"),
            redirect_stdout(io.StringIO()),
        ):
            selected = install.choose_one(console, "Choose destination", ["New", "Existing"])

        self.assertIsNone(selected)

    def test_checklist_back_keeps_current_selection_available(self) -> None:
        console = Console(no_color=True)
        with (
            patch.object(console, "ansi", True),
            patch("scripts.install.read_menu_key", return_value="left"),
            redirect_stdout(io.StringIO()),
        ):
            selected = install.choose_many(
                console,
                "Choose profiles",
                {"dotnet": ".NET", "react": "React"},
                initial_selection=["react"],
            )

        self.assertIsNone(selected)


class PathSafetyTests(unittest.TestCase):
    def test_destination_path_is_required_and_can_return_to_mode(self) -> None:
        console = Console(no_color=True)
        answers = iter(["", "b"])
        output = io.StringIO()
        with patch("builtins.input", side_effect=lambda _prompt: next(answers)), redirect_stdout(output):
            result = install.make_target(console, "New project folder")

        self.assertIsNone(result)
        self.assertIn("destination path is required", output.getvalue())

    def test_plan_rejects_parent_traversal(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPOSITORY_ROOT) as temporary:
            target = Path(temporary).resolve()
            item = PlannedFile(None, Path("../outside.txt"), "unsafe", content="no")
            with self.assertRaises(ValueError):
                make_plan(target, [item])

    def test_dry_run_does_not_create_a_new_destination(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPOSITORY_ROOT) as temporary:
            parent = Path(temporary).resolve()
            source_root = parent / "starter-pack-source"
            target = parent / "new-project"
            answers = iter(["1", str(target), "1", "0", "0", "0"])
            output = io.StringIO()
            with (
                patch("scripts.install.REPOSITORY_ROOT", source_root),
                patch("builtins.input", side_effect=lambda _prompt: next(answers)),
                redirect_stdout(output),
            ):
                result = install.main(["--dry-run", "--no-color"])

            self.assertEqual(result, 0)
            self.assertFalse(target.exists())
            self.assertIn("Preview complete", output.getvalue())


class InteractiveFlowTests(unittest.TestCase):
    def test_new_destination_offers_and_runs_git_init_only_after_yes(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPOSITORY_ROOT) as temporary:
            parent = Path(temporary).resolve()
            source_root = parent / "starter-pack-source"
            target = parent / "new-project"
            answers = iter(["1", str(target), "1", "0", "0", "0", "1", "y"])
            output = io.StringIO()
            with (
                patch("scripts.install.REPOSITORY_ROOT", source_root),
                patch("builtins.input", side_effect=lambda _prompt: next(answers)),
                patch.object(subprocess, "run") as run,
                redirect_stdout(output),
            ):
                result = install.main(["--no-color"])

            self.assertEqual(result, 0)
            run.assert_called_once_with(["git", "init", str(target)], check=True)
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertIn("Git repository initialized", output.getvalue())


class ConflictHandlingTests(unittest.TestCase):
    def test_existing_file_is_skipped_by_default_and_preserved(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPOSITORY_ROOT) as temporary:
            target = Path(temporary).resolve()
            existing = target / "AGENTS.md"
            existing.write_text("project rules", encoding="utf-8")
            source = target / "starter.md"
            source.write_text("starter rules", encoding="utf-8")
            planned = [(PlannedFile(source, Path("AGENTS.md"), "instructions"), existing)]

            with patch("builtins.input", return_value=""):
                installed, skipped, backups, failures = apply_plan(
                    Console(no_color=True), target, planned
                )

            self.assertEqual(installed, 0)
            self.assertEqual(skipped, 1)
            self.assertEqual(backups, [])
            self.assertEqual(failures, [])
            self.assertEqual(existing.read_text(encoding="utf-8"), "project rules")

    def test_confirmed_replace_backs_up_original_before_copy(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPOSITORY_ROOT) as temporary:
            target = Path(temporary).resolve()
            existing = target / "AGENTS.md"
            existing.write_text("project rules", encoding="utf-8")
            source = target / "starter.md"
            source.write_text("starter rules", encoding="utf-8")
            planned = [(PlannedFile(source, Path("AGENTS.md"), "instructions"), existing)]

            with patch("builtins.input", return_value="y"):
                installed, skipped, backups, failures = apply_plan(
                    Console(no_color=True), target, planned
                )

            self.assertEqual(installed, 1)
            self.assertEqual(skipped, 0)
            self.assertEqual(len(backups), 1)
            self.assertEqual(failures, [])
            self.assertEqual(existing.read_text(encoding="utf-8"), "starter rules")
            self.assertEqual(backups[0].read_text(encoding="utf-8"), "project rules")


if __name__ == "__main__":
    unittest.main()
