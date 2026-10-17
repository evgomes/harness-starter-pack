# Starter pack installer

The installer copies the English guidance into a new project folder or an existing repository. It requires Python 3.9+ and uses only the standard library. It runs on Windows, macOS, and Linux. It does not create an ASP.NET Core or React application; use the stack's own project generator for that.

## Run the wizard

Clone this repository, then run the command for your shell from the repository root:

| Platform / shell | Command |
|---|---|
| Windows PowerShell | `py -3 scripts/install.py` |
| Windows PowerShell without the `py` launcher | `python scripts/install.py` |
| macOS / Linux | `python3 scripts/install.py` |

The wizard asks whether to create a new project folder or add guidance to an existing repository, then asks for a filesystem path. It uses keyboard menus for the language, stack profiles, harnesses, and optional skills. For single-choice menus, use **Up/Down** and **Enter**. For multi-select menus, use **Up/Down** to move, **Space** to toggle items, **A** to toggle all, and **Enter** to confirm. Use **Left Arrow** to return to the previous step and **Right Arrow** to continue/select; the current selections are retained when revisiting a step. At the path prompt, enter **B** to return to destination mode or press **Enter** to keep the previously entered path. Press **Q** to cancel the wizard. Non-interactive terminals show equivalent text-menu choices. The destination mode and path must be valid before the wizard can continue; the language step requires an available language. Stack, harness, and skill selections may be empty. If you choose a new directory, the wizard offers to run `git init` after installing the files.

To review the planned files without creating the destination or writing anything, add `--dry-run`. To disable colored output, add `--no-color`; setting the standard `NO_COLOR` environment variable also disables color. Color is enabled only for supported interactive terminals.

## What gets installed

- Shared `AGENTS.md`, all five agreements (`architecture.md`, `dependencies.md`, `conventions.md`, `workflow.md`, and `quality-and-security.md`), common templates, hook guidance/examples, and guides are always copied.
- The portable skill library under `skills/`. This is a reference catalog; it does not activate every skill in a harness.
- Selected stack profiles under `stacks/` and selected harness setup notes under `harnesses/`. For a repository containing both technologies, select the combined ASP.NET Core + React profile; it includes the integrated guidance plus both individual profiles' technology-specific guidance. You can select individual profiles separately when you need only one stack. The installer copies guidance and templates, not application code or framework dependencies.
- `graphify` and `graphify-setup` are selected by default in the skill menu. You may deselect them. Other skills are opt-in, though supporting skills may be added automatically when a selected skill requires them.
- Selected skills are copied into the discovery folders of selected harnesses (`.agents/skills/` for Codex, Cursor, and OpenCode; `.claude/skills/` for Claude Code). If you select no harness, skills remain in the portable `skills/` reference library and are not activated in a harness. A skill may bring along another skill it links to, so copied references remain complete.
- Cursor rules and OpenCode configuration when those harnesses are selected. Claude Code gets a root `CLAUDE.md` entry point when selected. Codex uses the shared root `AGENTS.md`.

After installation, review the root instructions and tailor `docs/agreements/` to the actual project. If an existing file collides, the wizard skips it by default. It offers backup-and-replace for that individual file; choosing that option stores the original under `.harness-starter-backups/<timestamp>/` before copying the starter file. Nothing is deleted by the installer.

The wizard does not install harnesses or tools, download remote code, alter global settings, create application source code, change Git remotes, or overwrite existing files without confirmation. An existing harness config may contain project-specific settings; review its backup and merge required settings back into the installed starter config.

## Limitations

- The first installer version supports the complete English package only. Portuguese (Brazil) content is not presented as available until that package is ready.
- For projects using more than one harness, select each harness. Shared skill files may be copied into more than one harness-specific discovery folder.
- The root portable `skills/` directory contains the reference library. A preselected skill becomes discoverable only when at least one harness that supports project skills is selected.
- The console colors adapt to terminal support, `NO_COLOR`, and `--no-color`; color is decorative and does not encode information by itself.

## Manual alternative

You can also follow the [English package quick start](../en/README.md), then copy only the agreements, templates, stack profile, harness adapter, and skills the project needs. Manually merge existing harness instructions and settings instead of replacing them.
