---
name: feature-brainstorming
description: Optional pre-spec exploration for software changes whose problem, constraints, or solution options need clarification. Produces a concise exploration note and handoff for spec creation; does not implement code or make product decisions.
---

# Feature brainstorming

Use this skill only when exploration would help. If the engineer already knows the desired behavior and approach, skip it and proceed to the project spec or lightweight task contract.

## Inputs

Ask for or infer from the request: the idea/problem, target repository, known requirements, relevant docs/issues, constraints, and desired output location. Inspect the repository and its instruction files before proposing technical options. Ask only questions that cannot be resolved from available evidence and whose answer could change scope or design.

## Process

1. **Frame the need.** Summarize the current problem, desired outcome, users/actors, and likely scope. Separate confirmed facts from inference and open questions; cite project evidence as `path:line` where possible.
2. **Check context.** Read relevant instructions and agreements. Use Graphify for unfamiliar code relationships when available, then verify source. Search exact terms when exhaustive matching is required. Identify existing behavior, prior decisions, duplicates, and conflicts.
3. **Apply relevant lenses.** Consider domain rules, architecture, UX, OWASP/security, privacy, WCAG accessibility, operations, data migration, performance, and dependencies. Mark non-applicable lenses with a short reason; do not turn generic checklists into requirements.
4. **Compare options.** Present at least two materially different options when viable, including benefits, costs, risks, assumptions, and a recommendation only when useful. Suggest the smallest proof that would resolve an important uncertainty.
5. **Record the result.** Use `docs/templates/feature-exploration.md` and `docs/templates/handoff.md` in a task-specific folder agreed with the user. Do not overwrite existing artifacts. Keep the summary concise and preserve evidence links.
6. **Carry forward decisions.** Ask the responsible person to accept, reject, or adjust proposals. Record only decisions they made as decisions. Summarize accepted scope, non-goals, acceptance scenarios, proofs, and remaining questions as inputs to `docs/templates/spec.md`.

When moving from exploration to a feature spec, follow the project's branch-first workflow: inspect repository Git guidance and create/switch to the appropriate branch before drafting the spec. Brainstorming remains optional and does not replace engineer review of the spec's acceptance criteria.

## Boundaries

- This skill is discovery and option analysis, not implementation, final requirements approval, or legal/compliance advice.
- Label all novel behavior as a suggestion until an authorized project decision-maker accepts it.
- Do not invent user needs, existing system behavior, source-of-truth rules, or technical constraints.
- Do not send confidential source, secrets, or real personal data to external search or tools. Use sanitized examples.
- Keep brainstorming optional; do not add a mandatory approval checkpoint when the engineer has already specified the intended change.
