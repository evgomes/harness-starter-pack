# Harness Starter Pack

A collection of reusable instructions, skills, templates, and checks for AI-assisted software engineering. The initial package is in English and includes separate ASP.NET Core and React profiles that can be combined; additional stacks and a Brazilian Portuguese package are planned.

## Packages

- [English starter pack](en/README.md)
- [Português (Brasil)](pt-br/README.md)

## Getting started

Clone this repository, then choose the common guidance, a harness adapter, and a stack profile from `en/`. Review the project agreement templates and replace prompts and placeholders with the target project's actual decisions. Do not copy a template unchanged as if it described a project that has not been inspected.

The pack is also designed to be referenced directly by an agent. Start with `en/AGENTS.md` and load task-specific skills only when they apply.

To apply the English assets interactively to a new or existing project, use the [cross-platform installer](scripts/README.md). It uses Python's standard library and previews changes with `--dry-run`.

For the rationale and further reading behind the workflows and stack profiles, see [References and rationale](REFERENCES.md).

For agent visual checks in web apps, see the [browser testing guide](en/guides/browser-testing.md) and optional [browser visual validation skill](en/skills/browser-visual-validation/SKILL.md).

## Design principles

- One shared set of engineering agreements, with thin harness adapters.
- Skills for optional, multi-step workflows; concise always-on instructions for durable rules.
- Evidence before conclusions, especially in code review and security guidance.
- Cross-platform setup where practical, with platform-specific commands documented explicitly.
- Brainstorming is optional; spec-first or direct coding remains valid when the solution is already clear.
