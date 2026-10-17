# ASP.NET Core + React architecture prompts

> Verify every prompt against the target repository. Record accepted decisions in the project's shared `docs/agreements/architecture.md`; this file is a stack-specific starting point.

## System and ownership boundaries

- Identify the ASP.NET Core host, API transport, application/domain logic, persistence, external services, and React application entry points.
- State which side owns each invariant and decision. The server is authoritative for authorization, validation, and persisted domain state; browser checks improve usability but do not enforce security.
- Document deployment units, environments, origins, routing/reverse-proxy behavior, and how the UI reaches the API in development and production.

## API and UI contract

- Record API base-path/versioning, authentication mode, request/response DTO ownership, serialization conventions, pagination, and compatibility expectations.
- Define stable error responses and machine-readable error identifiers where the UI branches on failures. Explain how validation errors map to fields or page-level messages.
- Specify loading, empty, success, partial, and error states for important user flows, including retry and cancellation behavior where relevant.
- Describe how generated clients or shared schemas are produced and checked, if the project uses them. Do not share server domain entities directly with browser code by default.

## Data and trust boundaries

- Trace user identity and authorization from the browser request to server-side policy and data scoping. Identify CSRF, CORS, cookie/token storage, and redirect behavior applicable to the chosen authentication model.
- State which data may reach the browser, how secrets and sensitive values are excluded, and how logging/redaction works on both sides.
- Record ownership of timestamps, identifiers, tenancy, concurrency, and validation. The server persists canonical state; client caches and optimistic UI updates must reconcile with server responses.

## Cross-stack change impact

- For a change that alters both API and UI, describe rollout and compatibility order, including whether old clients or old servers must continue to work during deployment.
- Identify contract, integration, and end-to-end evidence needed in addition to backend and frontend unit/component checks.
- Record observability at the boundary: correlation identifiers, useful structured fields, privacy-safe diagnostics, and how a failed browser request can be traced to server logs.
