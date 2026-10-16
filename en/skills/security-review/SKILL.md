---
name: security-review
description: Threat-informed security review of a software change or design against project agreements and applicable OWASP guidance. Use alongside deterministic security tools; report concrete, evidence-backed risks without claiming certification.
---

# Security review

1. Read the project's threat model, architecture/security agreements, spec, and applicable privacy rules. Establish assets, actors, trust boundaries, entry points, and data flows.
2. Inspect the diff and relevant call paths for authentication/authorization, input validation, injection, output encoding, SSRF, deserialization, file handling, cryptography/secrets, dependency/supply-chain changes, logging, rate/resource exhaustion, and error disclosure as applicable.
3. For APIs, check server-side authorization at each protected operation and object/data scope. For React, assume browser code and client-side checks are untrusted; never put server secrets in the bundle.
4. Run only scanners or tests configured and approved for the project. Record scope, version, source freshness, exact result, and gaps. Do not treat a scanner's clean result as proof of security.
5. Report findings with an exploit scenario, affected boundary, impact, evidence (`path:line` or tool output), severity rationale, and remediation. Separate confirmed defects from hypotheses requiring validation.

Use current applicable OWASP resources such as [ASVS](https://owasp.org/www-project-application-security-verification-standard/) or [Top 10](https://owasp.org/www-project-top-ten/) as references, not as a substitute for a project threat model. Do not provide legal determinations. Do not exploit production systems or access data outside the authorized scope.
