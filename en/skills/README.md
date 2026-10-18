# Skills catalog

Skills are optional, task-scoped workflows that an agent loads when relevant. They are not all-on instructions, tools, or guarantees of review quality. The installer copies the portable catalog as reference material; it preselects `graphify` and `graphify-setup`, and copies selected skill folders into the discovery location of each compatible harness selected in the installer.

## Explore and understand

| Skill | What it does |
|---|---|
| [feature-brainstorming](feature-brainstorming/SKILL.md) | Clarifies an uncertain problem, constraints, and solution alternatives before a spec. Skip when the desired change is already clear. |
| [ui-design-exploration](ui-design-exploration/SKILL.md) | Researches and prototypes UI options before implementation when design direction is uncertain. |
| [graphify](graphify/SKILL.md) | Uses a fresh Graphify repository graph to navigate code relationships and impact paths. Graph findings should be confirmed against source. |
| [graphify-setup](graphify-setup/SKILL.md) | Ensures the Graphify CLI is installed in the developer's tool environment, then configures, refreshes, upgrades, or repairs the repository graph. |

## Review quality and risk

| Skill | What it does |
|---|---|
| [dependency-review](dependency-review/SKILL.md) | Reviews package inventory, licenses, advisories, updates, and scheduled audit findings. |
| [shift-left-code-review](shift-left-code-review/SKILL.md) | Performs a focused adversarial review of a complete spec-driven change and its final diff. |
| [security-review](security-review/SKILL.md) | Reviews a design or code change for threat-informed security issues and evidence. |
| [threat-modeling](threat-modeling/SKILL.md) | Creates a scoped threat model and connects concrete abuse scenarios to mitigations and verification. |
| [accessibility-review](accessibility-review/SKILL.md) | Checks UI changes against the project's accessibility target and relevant user flows. |

## Build and validate interaction

| Skill | What it does |
|---|---|
| [browser-visual-validation](browser-visual-validation/SKILL.md) | Inspects rendered web UI behavior, console/network output, and visual states in the available browser setup. |
| [hook-authoring](hook-authoring/SKILL.md) | Designs and validates optional repository or harness hooks, favoring deterministic, local, non-destructive checks. |

## Selection and dependencies

Graphify and Graphify setup are preselected in the installer, but can be deselected. When Graphify setup is selected, completing that workflow requires ensuring the CLI is installed on the developer's machine; the starter-pack installer itself does not install it. Skills are activated only if at least one supported harness is selected; otherwise they remain available in the portable `skills/` reference library. The installer may add supporting skills automatically: browser visual validation includes accessibility review, while UI design exploration includes accessibility review and browser visual validation. The exact harness discovery paths are described in [harnesses](../harnesses/README.md) and [installer guide](../../scripts/README.md).
