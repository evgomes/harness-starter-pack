# English starter pack

Reusable project guidance for AI-assisted software engineering. The content is organized into common agreements, optional workflow skills, harness adapters, and stack profiles.

## Quick start

To install the English guidance into a new or existing project from a clone of this repository, run the [cross-platform installer](../scripts/README.md). The manual steps below remain available when you want to choose and copy files yourself.

1. Read [AGENTS.md](AGENTS.md) and the [agreement catalog](docs/agreements/README.md); the installer copies all five agreements into the target project's `docs/agreements/` folder.
2. Copy or adapt the selected harness adapter from `harnesses/` into the target repository. Merge instructions with existing project files; do not overwrite local agreements blindly.
3. Start from the [spec template](docs/templates/spec.md) for work that needs an explicit contract. The [template index](docs/templates/README.md) includes verification, threat-model, risk-exception, hook-contract, and UI design exploration templates. Use the [feature brainstorming skill](skills/feature-brainstorming/SKILL.md) or [UI design exploration skill](skills/ui-design-exploration/SKILL.md) only when clarification or exploration would help; both are optional.
4. Select the [ASP.NET Core](stacks/aspnet-core/README.md) and/or [React](stacks/react/README.md) profile(s), or select the [combined ASP.NET Core + React profile](stacks/aspnet-core-react/README.md) when both live in the same repository. The combined installer option also includes both individual profiles' technology-specific guidance. Tailor the selected guidance to the actual repository.
5. Load relevant skills on demand. Start with [Graphify setup](skills/graphify-setup/SKILL.md) for Graphify installation, [dependency review](skills/dependency-review/SKILL.md) for package maintenance, and [shift-left review](skills/shift-left-code-review/SKILL.md) before a change is considered ready. Use [browser visual validation](skills/browser-visual-validation/SKILL.md) for browser-visible UI changes, [threat modeling](skills/threat-modeling/SKILL.md) when a change affects meaningful security or privacy boundaries, and [hook authoring](skills/hook-authoring/SKILL.md) when adding a project-specific lifecycle check.

## Clone and install

Clone this repository, change into its directory, and run the Python installer from the repository root. It requires Python 3.9+ and uses only the standard library:

```powershell
git clone https://github.com/evgomes/harness-starter-pack.git
cd harness-starter-pack
py -3 scripts/install.py
```

On macOS or Linux, run `python3 scripts/install.py`; on Windows without the `py` launcher, run `python scripts/install.py`. The wizard can add the English guidance to an existing repository or create a new project folder. It always copies all five agreements and the common template library. For a repository with both ASP.NET Core and React, select the combined profile; it includes its integrated guidance and both individual profiles. `graphify` and `graphify-setup` are preselected in the skills step; other skills are optional. Select at least one harness to copy the selected skills into its discovery folder. Review the preview and selected assets before applying them, then inspect the resulting changes and complete the project agreements with verified facts. Use `--dry-run` to preview without writing. The [installer guide](../scripts/README.md) describes choices, keyboard controls, collision handling, and limitations.

## Package map

| Area | Location | Purpose |
|---|---|---|
| Always-on guidance | `AGENTS.md` | Shared rules and navigation |
| Project agreements | `docs/agreements/` | Architecture, dependencies, conventions, workflow, quality and security |
| Reusable templates | `docs/templates/` | Specs, verification plans, threat models, risk exceptions, hook contracts, solution and UI exploration, handoffs, review reports |
| Optional skills | `skills/` | Graphify, brainstorming, UI design exploration, browser validation, dependency, security, threat modeling, hook authoring, accessibility, review workflows |
| Hook guidance | `hooks/` | Safe deterministic lifecycle checks, optional Graphify check, and vendor-neutral hook authoring |
| Harness adapters | `harnesses/` | Codex, Claude Code, Cursor, OpenCode |
| Stack profiles | `stacks/` | ASP.NET Core and React profiles, available separately or as a combined bundle for one repository |

## Skills and harnesses

The skills use the portable `SKILL.md` format. For project installation, Codex, Cursor, and OpenCode can use `.agents/skills/<skill-name>/`; Claude Code uses `.claude/skills/<skill-name>/`. Harness capabilities and supported formats can change, so check the linked official docs in each adapter before applying optional integrations.

The base `AGENTS.md` is the canonical instruction set. Harness-specific files should be thin entry points that preserve those agreements and explain any additional discovery behavior.

## Optional exploration and direct-to-spec paths

Use feature brainstorming when the problem, desired behavior, constraints, or implementation alternatives need exploration. For UI uncertainty, use UI design exploration to compare at least three researched ideas and prototype with mocked data. Both are optional. When the developer already knows what to build or design, skip exploration and go directly to the spec. Small, low-risk changes may follow a lightweight project workflow if its agreements allow that.

## References

- The root [References and rationale](../REFERENCES.md) guide explains the sources behind the spec/handoff workflow, slices, subagents, stack patterns, context management, and model selection.
- The Graphify setup and navigation skills are in `skills/graphify/` and `skills/graphify-setup/`.
- Brainstorming, handoff, slice, and shift-left review practices are in the corresponding skills, templates, and agreements.
- Harness documentation links are maintained in `harnesses/README.md`.
- [Browser testing and visual validation](guides/browser-testing.md) documents official setup sources and safe use across the supported harnesses.
