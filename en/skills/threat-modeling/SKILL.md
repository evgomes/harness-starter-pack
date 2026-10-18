---
name: threat-modeling
description: Create or update a scoped, evidence-oriented threat model for a software change, then connect scenarios to mitigations and verification. Use when a change affects identity, sensitive data, trust boundaries, external integrations, uploads, privileged operations, or abuse-sensitive behavior.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Threat modeling

Use this optional workflow when the change has meaningful security or privacy risk. Keep the model proportional to the scope; a focused change may need only a few concrete scenarios. Do not turn a checklist into a claim of security or compliance.

## Gather context

1. Read the relevant specification, architecture agreement, quality and security agreement, and existing threat model if present.
2. Inspect the changed flow and verify assumptions against code, configuration, tests, and deployment documentation.
3. Separate known facts from assumptions. Ask for missing context when it changes the threat or mitigation; otherwise record the assumption and its owner.
4. Set the scope and identify assets, actors, entry points, data stores, external dependencies, and trust boundaries. Use a small diagram if it clarifies the flow.

## Identify and assess scenarios

Describe threats as concrete scenarios: precondition, actor action, affected boundary or asset, and impact. Consider relevant STRIDE categories, abuse cases, privacy risks, and operational failure modes as prompts. Prioritize by plausible likelihood and impact using the project's risk method; do not rely on labels without rationale.

For each material scenario, identify prevention, detection, and recovery controls as applicable. Connect controls to observable verification evidence such as authorization tests, validation tests, configuration checks, or monitoring behavior. Do not claim a mitigation is effective until its implementation and evidence are checked.

## Record and connect

1. Create or update `docs/templates/threat-model.md` in the project and link it from the specification or change record.
2. Add the selected threat scenarios and evidence to the [verification plan](../../docs/templates/verification-plan.md).
3. Record unresolved accepted risks in `docs/templates/risk-exception.md`, with a risk owner, compensating controls, and review or expiry date.
4. State model limitations, assumptions, and checks not performed. Revisit the model when relevant trust boundaries, data, identity, or deployment assumptions change.

Use an applicable, versioned subset of [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) as testable requirements where useful. Do not infer that using ASVS, STRIDE, or this skill makes a system compliant or secure.

## References

- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
- [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)
