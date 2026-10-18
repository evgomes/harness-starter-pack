---
name: shift-left-code-review
description: Perform one adversarial review at the end of a complete spec-driven feature against its spec, project agreements, SOLID/Clean Code, security, accessibility, dependencies, and evidence. Report only concrete actionable findings; do not edit the change unless asked.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Shift-left code review

For spec-driven feature work, run this adversarial review once after all slices are complete and final verification has run. Do not repeat it per slice. If a strong review model is unavailable, the engineer can invoke this skill manually. Targeted verification after fixing findings is expected, but does not require a second adversarial review round unless the engineer explicitly requests one.

## Review inputs

Read the relevant spec/exploration decisions, `docs/agreements/architecture.md`, `conventions.md`, `quality-and-security.md`, the verification plan if present, and applicable stack/security/accessibility guidance. Inspect the actual diff and surrounding code. Use Graphify to locate impact paths when useful, then verify source and tests. If no spec exists, state the available contract and gaps rather than inventing requirements.

## Review steps

1. Map each acceptance criterion to changed code and available evidence.
2. Look for functional regressions, broken invariants, incomplete error paths, boundary violations, and unnecessary complexity against SOLID and Clean Code as interpreted by project agreements.
3. Check security/privacy concerns that apply: trust boundaries, authorization, validation, injection, secrets, sensitive logging, data exposure, unsafe dependency changes, and failure modes.
4. Check accessibility when UI changes: semantics, accessible names, keyboard access, focus order/visibility, errors/status messages, target size, zoom/reflow, and any project-specific WCAG criteria.
5. Check dependency and migration impacts. Verify whether required tests, lint, typecheck, build, scanners, or manual checks ran; distinguish “not run” from “failed.” Compare applicable checks and blocking thresholds with the project's quality and security agreement. Record any missing evidence in the verification plan or review report.
6. When a relevant threat model exists, verify that changed flows still match it and that planned mitigations have evidence. For material security or privacy changes without a model, consider whether the optional threat-modeling skill is warranted.
7. Report findings using `docs/templates/code-review.md` or the harness's review output. Sort by severity and cite tight `path:line` evidence. Identify each finding's source (tool, human reviewer, or model reviewer) and the rule/tool where known.

## Finding standard

Report a finding only when you can state: (a) the concrete scenario, (b) why the changed code causes a defect or violates an explicit contract, (c) user/security/operational impact, and (d) a practical correction. Do not report hypothetical edge cases without a path to occurrence, stylistic preferences without a local rule, or line changes that are merely nearby. Check whether an existing guard already prevents the issue.

Keep tool-generated findings and reviewer findings distinguishable. A scanner finding should include the tool or rule identifier and enough evidence to reproduce or verify it. A reviewer finding should identify the inspected path and reasoning. Do not repeat a scanner alert as an independently confirmed fact until its applicability is checked; document false positives, accepted risks, and unverified alerts honestly. Automated clean results do not prove security or correctness, and a model review does not replace deterministic checks or human accountability.

Use severity labels consistently with the project. If none exist, use Critical / High / Medium / Low and define impact in the report. Never claim a vulnerability, accessibility violation, or test result without supporting evidence. Findings remain suggestions until the project owner accepts them. Do not silently modify code during review.

## Closeout

Summarize reviewed scope, checks and evidence, unresolved gaps, and overall readiness. A clean review does not prove correctness or replace human review, CI, penetration testing, or accessibility testing.
