# Engineering workflow agreement

This agreement defines a reusable default workflow for AI-assisted changes. Adapt project-specific commands, branch conventions, approval gates, and delivery requirements to the target repository. The repository's verified architecture, conventions, and code patterns take precedence over generic guidance.

## Understand the project and request

1. Inspect the repository instructions, Git state, relevant source, tests, and existing documentation before proposing changes.
2. Read the project's architecture and conventions agreements, along with the relevant quality/security and dependency guidance. Learn the established patterns from nearby code before designing a change. Do not treat starter-pack examples as facts about the target project.
3. Summarize the request, scope, assumptions, relevant evidence, and material ambiguity before substantial implementation. Ask only when unresolved choices would materially change the work; otherwise state a reasonable assumption and proceed.
4. Exploration is optional. Use feature brainstorming when the problem or solution is unclear, and UI design exploration when screen or interaction alternatives need research and prototyping. If the intended solution is already clear, go directly to the specification or an appropriately lightweight task contract.

## Specification and approval

For meaningful behavior, cross-layer changes, security or privacy impact, data changes, or work that needs multiple slices, create a specification from [`docs/templates/spec.md`](../templates/spec.md) (or the selected stack profile's spec template). A small, low-risk change may use a lightweight task contract when project policy allows it.

Before drafting a spec, follow the repository's branch conventions and confirm the working tree and branch. The spec should state the user need, outcome, scope, existing behavior and architecture, constraints, assumptions to prove, acceptance criteria, risks, verification, and ordered slices. Keep facts, suggestions, and decisions distinct. The engineer reviews and adjusts acceptance criteria before accepting the spec and implementation begins.

## Proofs, slices, and implementation

- Identify assumptions that could invalidate the plan. When any require validation before implementation, make **Slice 1 the proof slice** and put those checks there. Record the method and result. If no pre-implementation proof is needed, Slice 1 is the first delivery slice.
- If a proof fails or changes the design, stop work that depends on it, explain the evidence and impact, and revise the spec with the engineer before proceeding.
- State slice order and subitems in the accepted spec. Complete each slice sequentially, subitem by subitem; do not start a later slice until all subitems in the current slice are complete and their evidence is recorded.
- Keep each delivery slice reviewable and coherent. Run focused checks for the changed behavior as work proceeds; run the required full suite and project-wide gates after all implementation slices, unless the project agreement or an accepted safety need requires an earlier run.
- Update the spec checklist and evidence as each subitem finishes. Keep a handoff current for spec-driven work, including branch, current slice/subitem, decisions, changed paths, checks, unresolved risks, and the exact next action.
- Do not silently change accepted scope, decisions, or project agreements. Record the proposed change and its impact, get the engineer's decision, then update the plan before continuing.

## Subagents and model selection

Use parallel subagents only when the user explicitly asks for them. Do not start delegated work merely because tasks appear independent or parallelism might save time.

When the user requests delegation, keep the primary agent responsible for orchestration, scope, architecture and security decisions, shared contracts, integration, verification, and final reporting. Prefer a strong reasoning-capable model for orchestration and ambiguous or high-impact decisions. A lower-cost model may handle a bounded implementation task when its contract is clear and its work can be independently verified. Give each delegate a scoped task, relevant decisions, file ownership, expected output, proof requirements, and a handoff; verify its result against source and the integrated change.

## Verification, review, and delivery

- Use deterministic local tools for formatting, linting, tests, dependency audits, and policy checks. Report exact commands and results; do not claim checks passed unless they ran successfully.
- Use a verification plan when checks span multiple layers or the change has meaningful security, privacy, accessibility, or operational risk. Use threat modeling when identity, sensitive data, trust boundaries, external integrations, privileged operations, or abuse risk are affected.
- For browser-visible UI changes, inspect the rendered behavior with the project's supported browser workflow and report which states and environments were exercised.
- After all implementation slices, perform exactly one adversarial review of the complete accepted spec and final diff. Use a strong model when available; otherwise the engineer can run the review skill manually. Resolve findings or document accepted exceptions with an owner, controls, and review date. AI review complements human review and CI; it does not replace them.
- Report what changed, evidence collected, checks run or deferred, review outcomes, and remaining risks. Keep the spec and handoff truthful to the final state.
