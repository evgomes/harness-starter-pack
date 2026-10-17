# Harness Starter Pack

A collection of reusable instructions, skills, templates, and checks for AI-assisted software engineering. The initial package is in English and includes ASP.NET Core and React profiles, separately and as a combined same-repository profile; additional stacks and a Brazilian Portuguese package are planned.

## Packages

- [English starter pack](en/README.md)
- [Português (Brasil)](pt-br/README.md)

## Getting started

### Clone and install

Clone the repository, change into its directory, and run the Python installer from the repository root (Python 3.9+):

```powershell
git clone https://github.com/evgomes/harness-starter-pack.git
cd harness-starter-pack
py -3 scripts/install.py
```

On macOS or Linux, run `python3 scripts/install.py`; on Windows without the `py` launcher, run `python scripts/install.py`. Review the preview and choices before applying the files. See the [installer guide](scripts/README.md) for interaction, options, and collision handling.

### Use the pack

Choose the common guidance, the adapter for your harness, and any applicable stack profile from `en/`. Copy all five common agreements to the target project's `docs/agreements/`; fill the architecture, dependency, conventions, and quality/security agreements with verified project decisions, and adapt the reusable workflow agreement only for documented project-specific needs. Select additional templates and skills as needed. Merge instructions with existing project files instead of overwriting established rules. Do not copy project agreement prompts unchanged as if they described a repository that has not been inspected.

The pack is also designed to be referenced directly by an agent. Start with `en/AGENTS.md` and load task-specific skills only when they apply.

To apply the English assets interactively to a new or existing project, use the [cross-platform installer](scripts/README.md). It uses Python's standard library and previews changes with `--dry-run`.

The installer always includes all five common agreements, shared templates, hook guidance/examples, guides, and the portable skill reference library. Select the combined ASP.NET Core + React profile for a co-located full-stack repository; it includes integrated guidance and both individual profiles' stack-specific guidance. You can select the profiles separately when you need just one stack. `graphify` and `graphify-setup` are preselected as skills; choose a harness to make selected skills discoverable to that agent. The installer does not install the Graphify tool itself.

For the rationale and further reading behind the workflows and stack profiles, see [References and rationale](REFERENCES.md).

For agent visual checks in web apps, see the [browser testing guide](en/guides/browser-testing.md) and optional [browser visual validation skill](en/skills/browser-visual-validation/SKILL.md).

## Design principles

- One shared set of engineering agreements, with thin harness adapters.
- Skills for optional, multi-step workflows; concise always-on instructions for durable rules.
- Evidence before conclusions, especially in code review and security guidance.
- Cross-platform setup where practical, with platform-specific commands documented explicitly.
- Brainstorming is optional; spec-first or direct coding remains valid when the solution is already clear.
