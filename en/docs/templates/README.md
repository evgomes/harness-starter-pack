# Templates

Copy the relevant template into the project documentation and tailor it to the work. Templates are starting structures, not mandatory ceremonies. Link completed artifacts from the specification, pull request, or handoff so reviewers can find the decision and evidence.

| Template | Use |
| --- | --- |
| [Specification](spec.md) | Define a feature or change before implementation when useful. |
| [Verification plan](verification-plan.md) | Plan tests and quality, security, and accessibility evidence for a change. |
| [Threat model](threat-model.md) | Record scoped assets, boundaries, concrete threats, and mitigations. |
| [Risk exception](risk-exception.md) | Document an accepted finding, compensating controls, owner, and review date. |
| [Hook contract](hook-contract.md) | Design and review an optional harness or repository hook. |
| [Exploration](feature-exploration.md) | Capture optional brainstorming and solution exploration. |
| [UI design exploration](ui-design-exploration.md) | Research design alternatives, prototype with mock data, and record the accepted direction before spec creation. |
| [Handoff](handoff.md) | Transfer context and outstanding work when a standard flow does not cover it. |
| [Code review](code-review.md) | Record review findings and their evidence. |
| [Harness setup overview](harness-readme.md) | Summarize installed starter-pack assets and give a project-specific configuration checklist and workflow examples. The installer generates `HARNESS-README.md` at the target repository root. |

## Stack-specific templates

When a project uses a supported stack profile, start from its focused templates and keep the shared template's project-level principles:

- [ASP.NET Core templates](../../stacks/aspnet-core/docs/templates/README.md) — API/domain specification, .NET verification plan, and ASP.NET Core threat-model prompts.
- [React templates](../../stacks/react/docs/templates/README.md) — UI specification, frontend verification plan, browser/client threat-model prompts, design prototype, and component styleguide entry.

See the [agreements index](../agreements/README.md) for project-level conventions.
