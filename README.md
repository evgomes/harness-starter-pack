# Harness Starter Pack

A collection of reusable instructions, skills, templates, and checks for AI-assisted software engineering. The initial package is in English and includes separate ASP.NET Core and React profiles that can be combined; additional stacks and a Brazilian Portuguese package are planned.

## Packages

- [English starter pack](en/README.md)
- [Português (Brasil)](pt-br/README.md)

## Getting started

### Clone and install

Clone the repository to a location where you can keep it available as a source for the starter assets:

```sh
git clone <repository-url>
cd harness-starter-pack
```

Run the Python installation script from the repository root, then review its choices and the files it adds to the target project. The script's path and command are documented in the [English package guide](en/README.md).

### Use the pack

Choose the common guidance, the adapter for your harness, and any applicable stack profile from `en/`. Copy all five common agreements to the target project's `docs/agreements/`; fill the architecture, dependency, conventions, and quality/security agreements with verified project decisions, and adapt the reusable workflow agreement only for documented project-specific needs. Select additional templates and skills as needed. Merge instructions with existing project files instead of overwriting established rules. Do not copy project agreement prompts unchanged as if they described a repository that has not been inspected.

The pack is also designed to be referenced directly by an agent. Start with `en/AGENTS.md` and load task-specific skills only when they apply.

For the rationale and further reading behind the workflows and stack profiles, see [References and rationale](REFERENCES.md).

For agent visual checks in web apps, see the [browser testing guide](en/guides/browser-testing.md) and optional [browser visual validation skill](en/skills/browser-visual-validation/SKILL.md).

## Design principles

- One shared set of engineering agreements, with thin harness adapters.
- Skills for optional, multi-step workflows; concise always-on instructions for durable rules.
- Evidence before conclusions, especially in code review and security guidance.
- Cross-platform setup where practical, with platform-specific commands documented explicitly.
- Brainstorming is optional; spec-first or direct coding remains valid when the solution is already clear.
