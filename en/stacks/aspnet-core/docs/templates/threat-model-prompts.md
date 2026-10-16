# ASP.NET Core threat-model prompts

Use these prompts as an extension to the shared [threat-model template](../../../../docs/templates/threat-model.md), not as a replacement. Answer only what applies and verify details against the actual application and hosting configuration.

## Boundaries and components

- Which endpoints, middleware, filters, handlers, hosted services, and external integrations participate?
- Where are the boundaries between HTTP transport, application/domain behavior, persistence, queues, and external services?
- Which identity, authentication scheme, authorization policy, tenant/owner scope, and service identity apply?
- Which data flows cross public networks, proxies, internal services, or process boundaries?

## ASP.NET Core-specific threat prompts

- Can an authenticated caller access another user's, tenant's, or object's data by changing an identifier or query filter?
- Are authorization checks enforced server-side for each operation and resource, including background or alternate entry points?
- Can binding, validation, serialization, or error handling disclose sensitive fields or accept unexpected values?
- Are CORS, antiforgery, cookie, token, forwarded-header, HTTPS, and proxy settings appropriate to the actual hosting topology?
- Can uploads, downloads, redirects, URL fetching, deserialization, or file paths cross intended boundaries?
- Do EF Core queries enforce ownership/tenant scope, bounded results, and safe handling of concurrency and transactions?
- Could retries, request size, rate, expensive queries, or fan-out enable resource exhaustion?
- Are secrets and personal data excluded from configuration examples, logs, exception details, and telemetry?
- Do migration, health, readiness, and background-job paths introduce privileged access or unsafe deployment assumptions?

For each applicable concern, record a concrete scenario and connect the mitigation to tests or configuration evidence. Do not assume a framework default is secure without confirming the effective project configuration.
