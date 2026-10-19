# Starter pack installer

The installer copies the selected language package (English or Brazilian Portuguese) into a new project folder or an existing repository. It requires [Python 3.9 or newer](https://www.python.org/downloads/) and uses only the standard library. It runs on Windows, macOS, and Linux. It does not create applications or install framework dependencies; use each stack's own project generator for that.

## Run the wizard

Clone this repository, then run the command for your shell from the repository root:

| Platform / shell | Command |
|---|---|
| Windows PowerShell | `py -3 scripts/install.py` |
| Windows PowerShell without the `py` launcher | `python scripts/install.py` |
| macOS / Linux | `python3 scripts/install.py` |

The wizard asks whether to create a new project folder or add guidance to an existing repository, then asks for a filesystem path. It uses keyboard menus for the language, stack profiles, harnesses, and optional skills. Choose **English** or **Português (Brasil)** before selecting package assets. For single-choice menus, use **Up/Down** and **Enter**. For multi-select menus, use **Up/Down** to move, **Space** to toggle items, **A** to toggle all, and **Enter** to confirm. Use **Left Arrow** to return to the previous step and **Right Arrow** to continue/select; the current selections are retained when revisiting a step. At the path prompt, enter **B** to return to destination mode or press **Enter** to keep the previously entered path. Press **Q** to cancel the wizard. Non-interactive terminals show equivalent text-menu choices. The destination mode and path must be valid before the wizard can continue; the language step requires an available language. Stack, harness, and skill selections may be empty. If you choose a new directory, the wizard offers to run `git init` after installing the files.

To review the planned files without creating the destination or writing anything, add `--dry-run`. To disable colored output, add `--no-color`; setting the standard `NO_COLOR` environment variable also disables color. Color is enabled only for supported interactive terminals.

## What gets installed

- Shared `AGENTS.md`, all five agreements, common templates, hook guidance/examples, and guides are always copied. English uses `docs/agreements/`; Brazilian Portuguese uses `docs/acordos/` and localized agreement filenames.
- A generated root `HARNESS-README.md` summarizes the actual selected stack profiles, harness adapters, and skills, then gives a project-specific setup checklist and example prompts. It is based on the [English template](../en/docs/templates/harness-readme.md) or [Portuguese template](../pt-br/docs/templates/readme-do-harness.md), according to the selected language. If that destination file already exists, normal collision handling applies: it is skipped by default or backed up before replacement after confirmation.
- The portable skill library under `skills/`. This is a reference catalog; it does not activate every skill in a harness.
- Selected stack profiles under `stacks/` and selected harness setup notes under `harnesses/`. Available profiles and candidate checks are listed in the [English stack catalog](../en/stacks/README.md) and [Portuguese stack catalog](../pt-br/stacks/README.md). For co-located applications, choose ASP.NET Core + React or Spring Boot + Angular; each bundle expands to integrated guidance plus its two individual profiles. Individual profiles can also be selected separately. The installer copies guidance and templates, not application code or framework dependencies.
- `graphify` and `graphify-setup` are selected by default in the skill menu. You may deselect them. Other skills are opt-in, though supporting skills may be added automatically when a selected skill requires them.
- Selected skills are copied into the discovery folders of selected harnesses (`.agents/skills/` for Codex, Cursor, and OpenCode; `.claude/skills/` for Claude Code). If you select no harness, skills remain in the portable `skills/` reference library and are not activated in a harness. A skill may bring along another skill it links to, so copied references remain complete.
- The [English skills catalog](../en/skills/README.md) and [Portuguese skills catalog](../pt-br/skills/README.md) summarize each skill, its use case, defaults, and supporting-skill dependencies.
- Cursor rules and OpenCode configuration when those harnesses are selected. Claude Code gets a root `CLAUDE.md` entry point when selected. Codex uses the shared root `AGENTS.md`.

After installation, review the root instructions and tailor the agreement folder to the actual project: `docs/agreements/` for English or `docs/acordos/` for Brazilian Portuguese. If an existing file collides, the wizard skips it by default. It offers backup-and-replace for that individual file; choosing that option stores the original under `.harness-starter-backups/<timestamp>/` before copying the starter file. For Portuguese installs, it can also offer to move a known legacy English-named file to its localized path; this requires confirmation and keeps a backup of the original. Other files are never removed by the installer.

Start with the generated root `HARNESS-README.md`: it lists the selected assets and provides the project-specific developer setup checklist. Complete and verify the project agreements, confirm the selected harness discovers its instructions/skills, decide which stack tool recommendations to adopt, and record actual build, test, lint, and security commands before using the workflow on project changes. When `graphify-setup` is selected (the default), complete its setup and ensure the Graphify CLI is installed in the developer's tool environment; the CLI is not an application dependency and the starter-pack installer does not install it. See the [post-installation checklist](../README.md#after-installing-into-a-project) for the full sequence.

The wizard does not install harnesses or tools, download remote code, alter global settings, create application source code, change Git remotes, or overwrite existing files without confirmation. An existing harness config may contain project-specific settings; review its backup and merge required settings back into the installed starter config.

## Limitations

- The installer supports the complete English and Brazilian Portuguese packages. Stack, harness, and skill selection identifiers stay stable internally; the Portuguese package localizes documentation paths, skill folders, and the agreement folder while preserving product names such as Graphify.
- For projects using more than one harness, select each harness. Shared skill files may be copied into more than one harness-specific discovery folder.
- The root portable `skills/` directory contains the reference library. A preselected skill becomes discoverable only when at least one harness that supports project skills is selected.
- The console colors adapt to terminal support, `NO_COLOR`, and `--no-color`; color is decorative and does not encode information by itself.

## Manual alternative

You can also follow the [English package quick start](../en/README.md) or [Portuguese package quick start](../pt-br/README.md), then copy only the agreements, templates, stack profile, harness adapter, and skills the project needs. Manually merge existing harness instructions and settings instead of replacing them.
