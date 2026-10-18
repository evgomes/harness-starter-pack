# English starter pack

Reusable project guidance for AI-assisted software engineering. The content is organized into common agreements, optional workflow skills, harness adapters, and stack profiles.

## Quick start

To install the English guidance into a new or existing project from a clone of this repository, install [Python 3.9 or newer](https://www.python.org/downloads/) and run the [cross-platform installer](../scripts/README.md), then select **English** in the language step. The manual steps below remain available when you want to choose and copy files yourself.

1. Read [AGENTS.md](AGENTS.md) and the [agreement catalog](docs/agreements/README.md); the installer copies all five agreements into the target project's `docs/agreements/` folder.
2. Copy or adapt the selected harness adapter from `harnesses/` into the target repository. Merge instructions with existing project files; do not overwrite local agreements blindly.
3. Start from the [spec template](docs/templates/spec.md) for work that needs an explicit contract. The [template index](docs/templates/README.md) includes verification, threat-model, risk-exception, hook-contract, and UI design exploration templates. Use the [feature brainstorming skill](skills/feature-brainstorming/SKILL.md) or [UI design exploration skill](skills/ui-design-exploration/SKILL.md) only when clarification or exploration would help; both are optional.
4. Choose applicable profiles from the [stack catalog](stacks/README.md): ASP.NET Core, React, Java + Spring Boot, Node.js + Express, Python + FastAPI, or Angular. For a co-located ASP.NET Core + React or Spring Boot + Angular repository, choose its combined profile; it adds integrated guidance and both individual profiles. Tailor recommendations to the actual repository.
5. Load relevant skills on demand. Start with [Graphify setup](skills/graphify-setup/SKILL.md) for Graphify installation, [dependency review](skills/dependency-review/SKILL.md) for package maintenance, and [shift-left review](skills/shift-left-code-review/SKILL.md) before a change is considered ready. Use [browser visual validation](skills/browser-visual-validation/SKILL.md) for browser-visible UI changes, [threat modeling](skills/threat-modeling/SKILL.md) when a change affects meaningful security or privacy boundaries, and [hook authoring](skills/hook-authoring/SKILL.md) when adding a project-specific lifecycle check.

## Clone and install

Install [Python 3.9 or newer](https://www.python.org/downloads/), clone this repository, change into its directory, and run the installer from the repository root. It uses only the Python standard library:

```powershell
git clone https://github.com/evgomes/harness-starter-pack.git
cd harness-starter-pack
py -3 scripts/install.py
```

On macOS or Linux, run `python3 scripts/install.py`; on Windows without the `py` launcher, run `python scripts/install.py`. The wizard can add English or Brazilian Portuguese guidance to an existing repository or create a new project folder. Select **English** to install this package. It always copies all five agreements and the common template library, and generates a root `HARNESS-README.md` tailored to the selected profiles, harnesses, and skills. Choose a combined stack profile when ASP.NET Core + React or Spring Boot + Angular live in one repository; each option includes integrated guidance and both individual profiles. `graphify` and `graphify-setup` are preselected in the skills step; other skills are optional. Select at least one harness to copy the selected skills into its discovery folder. Review the preview and selected assets before applying them, then use `HARNESS-README.md` to complete project setup before starting the workflow. Use `--dry-run` to preview without writing. The [installer guide](../scripts/README.md) describes choices, keyboard controls, collision handling, and limitations.

### After installation

Treat the target project's generated `HARNESS-README.md` as the developer-facing onboarding checklist. Work through it before relying on the workflow:

1. Confirm the selected assets and resolve any preview conflicts. Existing files are skipped unless replacement was explicitly approved.
2. Inspect project source, dependency manifests, CI, and deployment configuration. Complete the architecture, dependencies, conventions, and quality/security agreements with verified project decisions. Keep the shared workflow agreement as the reusable default unless documented project needs call for adapting it.
3. Review each selected stack profile. Decide which recommendations apply, select actual libraries and versions, and document build, test, lint, security, and quality commands from the repository. The installer does not install application dependencies or recommended tooling.
4. Verify harness instruction and skill discovery, and merge harness configuration with existing settings. When `graphify-setup` is selected (the installer default), complete its setup and ensure the Graphify CLI is installed on the developer's machine. It is a developer tool, not an application dependency; the starter-pack installer copies instructions but does not install the CLI.
5. For substantial work, use the common or stack-specific spec and verification templates. Reserve slice 1 for proof work when an assumption needs validation; then deliver remaining slices in order, one subitem at a time.
6. Run the agreed baseline checks and record commands and results. Setup is complete when the agreements, tool choices, harness discovery, and expected checks are understood and documented.

## Package map

| Area | Location | Purpose |
|---|---|---|
| Always-on guidance | `AGENTS.md` | Shared rules and navigation |
| Project agreements | `docs/agreements/` | Architecture, dependencies, conventions, workflow, quality and security |
| Reusable templates | `docs/templates/` | Specs, verification plans, threat models, risk exceptions, hook contracts, solution and UI exploration, handoffs, review reports |
| Optional skills | `skills/` | Graphify, brainstorming, UI design exploration, browser validation, dependency, security, threat modeling, hook authoring, accessibility, review workflows |
| Hook guidance | `hooks/` | Safe deterministic lifecycle checks, optional Graphify check, and vendor-neutral hook authoring |
| Harness adapters | `harnesses/` | Codex, Claude Code, Cursor, OpenCode |
| Stack profiles | `stacks/` | Six individual technology profiles plus ASP.NET Core + React and Spring Boot + Angular bundles; see [stack catalog](stacks/README.md) |

## Skills and harnesses

The skills use the portable `SKILL.md` format. For project installation, Codex, Cursor, and OpenCode can use `.agents/skills/<skill-name>/`; Claude Code uses `.claude/skills/<skill-name>/`. Harness capabilities and supported formats can change, so check the linked official docs in each adapter before applying optional integrations.

See the [skills catalog](skills/README.md) for an overview of all available workflows, when to use them, installer defaults, and automatically included supporting skills.

The base `AGENTS.md` is the canonical instruction set. Harness-specific files should be thin entry points that preserve those agreements and explain any additional discovery behavior.

## Optional exploration and direct-to-spec paths

Use feature brainstorming when the problem, desired behavior, constraints, or implementation alternatives need exploration. For UI uncertainty, use UI design exploration to compare at least three researched ideas and prototype with mocked data. Both are optional. When the developer already knows what to build or design, skip exploration and go directly to the spec. Small, low-risk changes may follow a lightweight project workflow if its agreements allow that.

## References

- The root [References and rationale](../REFERENCES.md) guide explains the sources behind the spec/handoff workflow, slices, subagents, stack patterns, context management, and model selection.
- The Graphify setup and navigation skills are in `skills/graphify/` and `skills/graphify-setup/`.
- Brainstorming, handoff, slice, and shift-left review practices are in the corresponding skills, templates, and agreements.
- Harness documentation links are maintained in `harnesses/README.md`.
- [Browser testing and visual validation](guides/browser-testing.md) documents official setup sources and safe use across the supported harnesses.
