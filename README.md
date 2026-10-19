# Harness Starter Pack

A collection of reusable instructions, skills, templates, and checks for AI-assisted software engineering. Complete English and Brazilian Portuguese packages are available. Both include ASP.NET Core, React, Java + Spring Boot, Node.js + Express, Python + FastAPI, and Angular profiles, plus same-repository bundles for ASP.NET Core + React and Spring Boot + Angular.

## Packages

- [Leia este README em português (Brasil)](README.pt-br.md)
- [English starter pack](en/README.md)
- [Português (Brasil)](pt-br/README.md)

## Getting started

### Clone and install

Install [Python 3.9 or newer](https://www.python.org/downloads/), clone the repository, change into its directory, and run the installer from the repository root:

```powershell
git clone https://github.com/evgomes/harness-starter-pack.git
cd harness-starter-pack
py -3 scripts/install.py
```

On macOS or Linux, run `python3 scripts/install.py`; on Windows without the `py` launcher, run `python scripts/install.py`. Review the preview and choices before applying the files. See the [installer guide](scripts/README.md) for interaction, options, and collision handling.

### Use the pack

Choose the language in the installer, then select common guidance, the adapter for your harness, and applicable stack profiles from that language package (`en/` or `pt-br/`). The English package installs agreements under `docs/agreements/`; Brazilian Portuguese installs them under `docs/acordos/` with localized filenames. Fill the architecture, dependency, conventions, and quality/security agreements with verified project decisions, and adapt the reusable workflow agreement only for documented project-specific needs. Select additional templates and skills as needed. Merge instructions with existing project files instead of overwriting established rules. Do not copy project agreement prompts unchanged as if they described a repository that has not been inspected.

The pack is also designed to be referenced directly by an agent. Start with `AGENTS.md` in the chosen language package and load task-specific skills only when they apply.

To apply either language package interactively to a new or existing project, use the [cross-platform installer](scripts/README.md). It uses Python's standard library and previews changes with `--dry-run`.

The installer always includes all five common agreements, shared templates, hook guidance/examples, guides, and the portable skill reference library in the chosen language. It also generates `HARNESS-README.md` at the target root with a summary of selected assets, setup steps, and example prompts. Stacks are opt-in. Select ASP.NET Core + React or Spring Boot + Angular when both applications share a repository; each bundle includes integrated guidance and its two individual profiles. See the relevant [English](en/stacks/README.md) or [Portuguese](pt-br/stacks/README.md) stack catalog. `graphify` and `graphify-setup` are preselected as skills; choose a harness to make selected skills discoverable to that agent. See the corresponding [English](en/skills/README.md) or [Portuguese](pt-br/skills/README.md) skill catalog. The installer does not install Graphify or application dependencies.

### After installing into a project

Use the generated `HARNESS-README.md` in the target project as the developer's setup checklist. The reusable [HARNESS-README template](en/docs/templates/harness-readme.md) shows its structure. Before relying on the workflow:

1. Confirm the listed stack profiles, harness adapters, skills, and discovery paths match the intended setup. Resolve any install preview conflicts; existing files are skipped unless replacement was explicitly approved.
2. Inspect the target repository's source, manifests, CI, and deployment configuration. Fill `docs/agreements/architecture.md`, `dependencies.md`, `conventions.md`, and `quality-and-security.md` with verified project decisions. Keep `workflow.md` as the reusable default unless the project has documented workflow requirements that call for adapting it.
3. Review each selected profile and decide which architecture/convention recommendations apply. Choose actual libraries and versions, and define build, test, lint, security, and quality commands from the project itself. The installer copies recommendations; it does not install framework packages, linters, or test tools.
4. Check that the selected harness discovers the installed instructions and skills. Review and merge harness configuration with existing project settings instead of replacing project-specific configuration blindly.
5. If `graphify-setup` is selected (the installer selects it by default), follow `skills/graphify-setup/SKILL.md` and ensure the Graphify CLI is installed in the developer's tool environment. The CLI is separate from application dependencies; the starter-pack installer does not install it.
6. For a substantial change, start from the common or stack-specific spec template and define acceptance and verification evidence. Use slice 1 for proof work when an assumption needs validation; then complete the remaining slices sequentially, subitem by subitem.
7. Run the agreed baseline checks and record actual commands and results before treating the harness setup as complete.

The target project's generated `HARNESS-README.md` summarizes its specific selections and links to the corresponding profile docs. The [English quick start](en/README.md), [Portuguese quick start](pt-br/README.md), and [installer guide](scripts/README.md) provide the detailed asset catalog and installer behavior.

For the rationale and further reading behind the workflows and stack profiles, see [References and rationale](REFERENCES.md).

For agent visual checks in web apps, see the [browser testing guide](en/guides/browser-testing.md) and optional [browser visual validation skill](en/skills/browser-visual-validation/SKILL.md).

## Design principles

- One shared set of engineering agreements, with thin harness adapters.
- Skills for optional, multi-step workflows; concise always-on instructions for durable rules.
- Evidence before conclusions, especially in code review and security guidance.
- Cross-platform setup where practical, with platform-specific commands documented explicitly.
- Brainstorming is optional; spec-first or direct coding remains valid when the solution is already clear.

## License

This repository is licensed under the [MIT License](LICENSE).
