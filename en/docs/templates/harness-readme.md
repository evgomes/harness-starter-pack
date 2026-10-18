# Harness setup overview

This project received a tailored set of AI-assisted engineering guidance from Harness Starter Pack. This overview records the installed assets and the setup work to do before relying on the workflow. The installer does not install frameworks, application dependencies, harness products, or external tools.

For manual use, replace every `{{...}}` placeholder with the selected project assets and remove any sections that do not apply. The installer fills these sections automatically.

## Installation summary

{{INSTALLATION_SUMMARY}}

### Core guidance copied to every installation

- [AGENTS.md](AGENTS.md): shared agent instructions and workflow entry point.
- [Project agreements](docs/agreements/README.md): architecture, dependencies, conventions, workflow, and quality/security. Complete the project-specific agreements before treating recommendations as settled decisions.
- [Shared templates](docs/templates/README.md): feature specs, verification plans, threat models, handoffs, and other optional artifacts.
- `hooks/` and `guides/`: optional setup guidance and examples; hooks are not silently enabled.
- `skills/`: portable reference library. Only selected workflows are copied to a harness discovery folder.

### Selected stack profiles

{{STACK_PROFILES}}

### Selected harnesses

{{HARNESSES}}

### Selected skills

{{SKILLS}}

## Setup checklist before regular use

1. Read this file, [AGENTS.md](AGENTS.md), and the installed harness adapter(s) above. Confirm how your selected agent discovers project instructions and skills.
2. Inspect the real repository structure, manifests, CI, deployment files, and existing conventions. Complete [architecture](docs/agreements/architecture.md), [dependencies](docs/agreements/dependencies.md), [conventions](docs/agreements/conventions.md), and [quality and security](docs/agreements/quality-and-security.md) with verified project decisions. Keep the shared [workflow agreement](docs/agreements/workflow.md) as the reusable default; adapt it only to documented project-specific process.
3. For each selected stack, review its profile and any supplemental architecture/convention prompts below. Decide which guidance applies, record accepted project-specific decisions in the root agreements, and link to supporting docs if you retain them separately.
4. Resolve package/library choices, versions, build and test commands, linters, security/dependency checks, and CI gates from the actual project. Profile tools are recommendations; the installer has not installed them.
5. If `graphify-setup` is selected (the installer selects it by default), complete the [Graphify setup skill](skills/graphify-setup/SKILL.md) and ensure the CLI is installed in the developer's tool environment. Graphify is a developer tool, not an application dependency; the starter-pack installer copies its instructions but does not install the CLI.
6. Before a substantial change, use the common or stack-specific spec template. If an assumption needs proof, make slice 1 the proof slice; then work through all remaining slices in order, one subitem at a time. Record focused verification as you go and required full-suite evidence at the end.

### Stack-specific follow-up

{{STACK_SETUP}}

## Example prompts

Use or adapt these requests after reviewing the repository:

> Read `HARNESS-README.md`, `AGENTS.md`, and the applicable project aEgreements. Inspect the repository's actual manifests and CI. Report which setup checklist items remain unresolved; do not treat generic profile recommendations as adopted decisions.

> I want to implement [feature]. First inspect the relevant code and completed agreements. Draft a spec using [the relevant template](docs/templates/README.md), identify assumptions that need a proof slice, then propose ordered slices with acceptance and verification evidence. Do not begin implementation until I review the spec.

For a small, clear change, follow the project workflow's lightweight path rather than creating ceremony that the change does not need.

## Maintenance

Update this overview when harnesses, skills, stack profiles, or project setup decisions change. If the installer reported an existing-file conflict for this document, it was skipped unless you explicitly chose backup-and-replace; review the file plan and merge the generated overview with any local content.
