# Engineering workflow agreement

> Status: starter template. Align required gates and approvals with the actual repository and delivery process.

## Choose the path

1. **Optional exploration:** when the problem, constraints, or solution options need clarification, run the `feature-brainstorming` skill. For screen/interaction design uncertainty, use the optional `ui-design-exploration` skill to research and prototype before spec creation. If the engineer already knows the intended behavior/design, skip exploration and proceed to the spec or lightweight task contract.
2. **Branch:** before drafting a feature spec, inspect repository Git guidance and create or switch to the appropriate feature branch. Follow its naming and base-branch rules; confirm the working tree and branch before editing.
3. **Spec:** use the shared or stack-specific spec template for meaningful behavior, cross-layer impact, security/privacy, data changes, or multi-slice work. Include an “As a user, I want…” summary, in/out scope, context, acceptance criteria, and slices. The engineer reviews and adjusts acceptance criteria before accepting the spec and beginning implementation.
4. **Proofs and slices:** identify assumptions that could invalidate the design. If a proof is needed to validate the approach and avoid changing the guidance/spec later, make it Slice 1. Otherwise, make the first delivery slice Slice 1. Define ordered subitems, acceptance evidence, and completion status for every slice.
5. **Implementation:** execute slices and subitems strictly in the agreed order. Do not skip, defer silently, or start a later slice until every item in the current slice is complete and its evidence is recorded. Run focused tests/checks for the current slice; defer the full test suite to the end of the spec implementation unless a repository agreement or an explicitly accepted safety need requires an earlier run.
6. **Progress records:** update the spec's subitem status and evidence and the feature handoff as each item finishes, before moving to the next item. Keep the current slice, completed work, decisions, changed paths, verification, risks, and exact next action resumable.
7. **Amendments:** if implementation needs to deviate from the accepted spec or project agreements, stop affected work, document the proposed change and reason in the spec amendment log, identify impact to scope/slices/acceptance/evidence, and get the engineer's decision before proceeding. Record the accepted decision and source; do not silently replan.
8. **Final verification and review:** after all slices, run the required full test suite and project-agreed checks, then perform one adversarial review round against the complete spec and final diff. Use a strong model when available; otherwise the engineer can run the `shift-left-code-review` skill manually. Do not run an adversarial review on every slice. Resolve or document findings and record final evidence.
9. **Handoff and delivery:** keep the handoff current through completion and report actual outcomes, outstanding risks, and checks.

## Specs and decisions

An exploration report contains facts, inferences, suggestions, and human decisions separately. Only accepted decisions become requirements. The spec is the implementation contract; it links to the exploration and records the approved summary, scope, context, alternatives, engineer-reviewed acceptance criteria, ordered slice checklist, risks, and verification evidence. Keep an amendment log for every accepted deviation, including who/what authorized it and which plan/evidence changed.

## Subagents and model choice

Do not assume subagents or parallel work are required. Use subagents only when the developer asks for them. When requested, the orchestrator retains responsibility for framing, architecture/security decisions, reconciliation, and final review; delegate bounded tasks with enough repository/spec/agreement context, file ownership, constraints, output, verification evidence, and handoff expectations. Prefer lower-cost models for clear, bounded implementation tasks when available; reserve stronger reasoning for ambiguous/high-impact decisions and the final adversarial review. Verify all delegated work against source and the integrated diff.

## Git worktrees

Do not assume parallel work or worktrees. Use a worktree when the developer requests isolated/parallel work, or repository workflow requires it. Before creating one, confirm the intended branch/base and whether the worktree should include existing changes. Assign non-overlapping files or explicit ownership and keep shared contracts, migrations, and integration points under one owner. A single sequential feature flow normally stays on its feature branch.

## Handoffs

Create a feature handoff when starting spec-driven implementation, using `docs/templates/handoff.md` or the repository's equivalent. Update it with the spec after every completed subitem, and before any pause or transition. Include status, branch, current slice/subitem, decisions, changed paths, focused commands/results, pending items, risks, and the exact next action. Avoid replaying the whole conversation.

## Reporting cadence

Time-boxed progress reports and periodic check-ins are optional. Follow an explicit developer preference; otherwise work with reasonable autonomy and report at meaningful milestones, when blocked or awaiting a decision, and at completion. Do not interrupt sequential implementation solely to satisfy a default timer.

## Completion

Every slice subitem is complete or explicitly amended/deferred with engineer approval; the full test suite and required project checks have end-of-spec results or documented gaps; exactly one adversarial review round has been recorded; dependency records and agreements are current; findings and amendments are traceable; the handoff and final report reflect reality.
