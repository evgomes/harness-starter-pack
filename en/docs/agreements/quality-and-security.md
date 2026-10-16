# Quality and security agreement

This agreement defines how a project makes quality and security checks repeatable. It does not prescribe a specific scanner, CI provider, hook framework, or numeric threshold. Record the project's selected tools, commands, thresholds, and owners in this document or the relevant project configuration.

## Principles

- Validate behavior with tests and observable evidence. A clean scanner report does not prove that a system is secure or correct.
- Prefer checks that are deterministic, explainable, and actionable. Keep fast feedback close to the change and run broader checks in CI or scheduled workflows.
- For legacy systems, distinguish findings introduced by a change from existing debt. Track existing findings so the baseline does not hide regressions.
- Use SOLID and Clean Code as design and review prompts, applied in context rather than as mechanical scoring rules.
- Do not impose a universal coverage percentage or complexity limit. Set thresholds that fit the project, explain exceptions, and prevent a change from making the agreed baseline worse.
- Treat tool output and human/model review as different evidence sources. Confirm material findings against the code, configuration, and applicable project requirements.
- Keep local hooks useful and fast. CI or another protected, auditable process is the authoritative merge gate; local hooks can be skipped or unavailable.
- Do not claim compliance or certification from a subset of checks. If useful, select and record applicable, versioned requirements from a framework such as OWASP ASVS.

## Project validation catalog

For each applicable row, record the actual command or stable project entry point, trigger, blocking policy, owner, and evidence location. Remove rows that do not apply and add project-specific checks.

| Check area | Purpose | Project command or entry point | Local trigger | CI or scheduled trigger | Blocking policy / owner |
| --- | --- | --- | --- | --- | --- |
| Build and type validation | Detect compilation and type errors |  |  |  |  |
| Automated tests | Verify behavior at relevant levels |  |  |  |  |
| Coverage | Show untested behavior and change trends |  |  |  |  |
| Formatting, lint, and static analysis | Keep style and common defects consistent |  |  |  |  |
| Complexity and duplication | Surface difficult or repeated code for review |  |  |  |  |
| Source security analysis | Find code patterns that may cause vulnerabilities |  |  |  |  |
| Dependency and update review | Identify vulnerable, outdated, or unmaintained packages |  |  |  |  |
| License review | Check package license obligations against project policy |  |  |  |  |
| Secrets and configuration | Detect exposed credentials and unsafe defaults |  |  |  |  |
| Accessibility | Validate relevant WCAG expectations and user flows |  |  |  |  |
| Other project-specific checks |  |  |  |  |  |

## Threshold and finding policy

For coverage, complexity, duplication, and static-analysis findings, document:

- the scope being measured (for example, changed code, a component, or the whole repository);
- the selected threshold and why it is useful for this project;
- how new findings are distinguished from accepted legacy findings;
- which findings block merging and who can approve an exception;
- where reports and evidence are retained.

Avoid optimizing a metric at the expense of readable design or meaningful tests. A threshold is a prompt for investigation, not a substitute for engineering judgment.

For security checks, record the scanner or review method, coverage limits, severity policy, triage owner, and remediation expectations. Verify consequential reports rather than treating a tool's severity label as a complete risk assessment. Manual review should consider trust boundaries, authorization, data handling, failure behavior, and abuse cases that automated rules may not see.

## Threat modeling and risk acceptance

Use the optional [threat-modeling skill](../../skills/threat-modeling/SKILL.md) for changes that introduce or materially change authentication, authorization, sensitive data handling, external integrations, uploads, privileged operations, trust boundaries, or abuse-sensitive business behavior. Store a scoped model using the [threat-model template](../templates/threat-model.md) and link it from the relevant specification.

Record accepted risks with the [risk-exception template](../templates/risk-exception.md), including an accountable owner, compensating controls, and a review or expiry date. An exception documents a project decision; it does not establish legal or regulatory compliance.

## Related project agreements

- [Architecture agreement](architecture.md)
- [Dependency agreement](dependencies.md)
- [Conventions agreement](conventions.md)
- [Workflow agreement](workflow.md)
- [Verification-plan template](../templates/verification-plan.md)

## References

- [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
- [OWASP Software Supply Chain Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html)
