# Shared agent instructions

This file is a starting point for a target software project. Adapt it to the actual repository before relying on it. Project-specific decisions in `docs/agreements/` take precedence over generic suggestions here.

## First steps

1. Inspect the repository, its Git state, existing instructions, build/test commands, and relevant documentation.
2. Read only the agreement sections relevant to the task. Do not load every skill or document by default.
   - For behavior, security, quality, or dependency changes, consult the applicable parts of `docs/agreements/quality-and-security.md` and `docs/agreements/dependencies.md`.
3. For an unfamiliar code path, use Graphify if the project has it. Before the first query in a task, refresh or check freshness with the script for the available runtime: `pwsh <skill-path>/scripts/refresh-graph.ps1` on PowerShell, or `bash <skill-path>/scripts/refresh-graph.sh` on macOS/Linux (Python 3 required). Refresh again after source changes before finishing. If the session-start hook reports missing setup or a stale index, follow the `graphify-setup` or `graphify` skill; never query a stale graph. Verify graph results against source and tests. Use exact search for exhaustive string or call-site checks.
4. State your understanding, scope, assumptions, and evidence before substantial implementation.

## Choose a workflow proportionate to the task

- **Optional feature brainstorming:** use the `feature-brainstorming` skill when the problem or solution needs clarification, when alternatives matter, or when unresolved constraints could change the design. Skip it when the engineer already knows the intended behavior and approach.
- **Optional UI design exploration:** when the engineer wants to choose a screen or interaction direction before a spec, use `ui-design-exploration`. Research at least three ideas, prototype with the actual stack and mocked data, and add reusable components to the existing design system/styleguide. After the engineer selects a direction, hand the behavior and design decisions into the branch-first spec workflow.
- **Understand, then spec:** before proposing a design, read the project's architecture and conventions agreements and study nearby source patterns. Before drafting a feature spec, inspect Git guidance and create/switch to the required feature branch. For meaningful behavior, cross-layer impact, security/privacy implications, data changes, or multiple slices, use `docs/templates/spec.md` or the relevant stack-specific template. Include the user need, scope, context, assumptions, acceptance criteria, risks, verification, and ordered slices. The engineer reviews and adjusts acceptance criteria before accepting the spec and implementation starts.
- **Proof-first slice:** when an assumption needs pre-implementation validation, make Slice 1 the proof slice. Otherwise Slice 1 is the first delivery slice. Complete remaining slices sequentially, subitem by subitem; do not start a later slice before every current-slice item is complete and evidenced.
- **Verification planning:** use `docs/templates/verification-plan.md` when checks span multiple layers or the change has meaningful security, privacy, accessibility, or operational risk. Record what ran and what did not.
- **Threat modeling:** load the optional `threat-modeling` skill when changes affect identity, sensitive data, trust boundaries, external integrations, uploads, privileged operations, or abuse-sensitive behavior.
- **Implementation:** keep changes scoped and reviewable. Run only tests/checks scoped to the active slice during implementation. Save the full test suite for after all spec slices, unless a repository agreement or accepted spec amendment requires an earlier run. Update the spec's subitem status/evidence and the handoff after each completed item, before advancing.
- **Amendments:** do not silently deviate from the accepted spec or project agreements. Stop affected work, record the proposed deviation, reason, and impact in the spec amendment log, obtain the engineer's decision, then update the plan and proceed.
- **Handoff:** create a handoff for spec-driven implementation and keep it aligned with the spec after each item, on pauses/transitions, and at completion. Include branch, current slice/subitem, evidence, blockers, and the exact next action.
- **Review:** run exactly one adversarial review round at the end of the complete spec implementation, against all requirements and the final diff. Use a strong model if available; otherwise the engineer may run the `shift-left-code-review` skill manually. Do not adversarially review every slice.
- **Risk exceptions:** document accepted unresolved findings with `docs/templates/risk-exception.md`, including an accountable owner, compensating controls, and review date.

## Engineering standards

- Follow the project's architecture and stack profile. Apply SOLID and Clean Code as tools for clarity, testability, and change isolation, not as a reason to add abstractions without need.
- Treat security, privacy, accessibility, reliability, and data integrity as part of the feature contract when applicable.
- For browser-visible UI changes, validate the rendered behavior in branded Chrome when available. Use the `browser-visual-validation` skill for a focused inspection and report accurately when only an embedded or Chromium browser is available; see `guides/browser-testing.md` for harness setup and safety guidance.
- Prefer deterministic local tools for linting, formatting, tests, dependency audits, and policy checks. Report the exact commands and results; never claim a check passed unless it ran successfully.
- Do not add dependencies without checking purpose, maintenance, license, transitive risk, and security status, then updating `docs/agreements/dependencies.md` in the same change.
- Never log or place secrets or real personal data in prompts, handoffs, test fixtures, or review output.

## Delegation and worktrees

Use parallel subagents only when the developer explicitly asks. When asked, keep orchestration, architecture/security decisions, integration, verification, and final decisions with the primary agent. Prefer a strong reasoning-capable model for orchestration and ambiguous/high-impact choices; a lower-cost model can implement bounded, well-specified tasks whose results can be verified. Give each delegate repository/spec/agreement context, a bounded task, file ownership, expected evidence, constraints, and handoff. Use Git worktrees when requested or required by project workflow for isolation. Do not parallelize shared contracts or migrations without an agreed interface.

Time-boxed reports and periodic check-ins are optional. Follow an explicit developer preference; otherwise work with reasonable autonomy and report at milestones, blockers/decision points, and completion.

## Completion report

Summarize behavior changed, files or contracts affected, checks actually run, review findings resolved, and material limitations. Leave the repository's workflow and handoff current when the work is not fully complete.
