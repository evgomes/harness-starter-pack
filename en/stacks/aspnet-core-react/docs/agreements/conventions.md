# ASP.NET Core + React conventions prompts

> Suggested defaults for a repository containing both stacks. Keep only conventions that fit the project and record accepted choices in its shared `docs/agreements/conventions.md`.

## Boundaries and contracts

- Keep server domain/application types independent from HTTP DTOs and browser view models unless a deliberate contract-generation approach says otherwise.
- Keep API mapping and transport concerns at the ASP.NET Core boundary. Keep React components focused on presentation and interaction; put reusable client behavior in explicit modules.
- Validate all untrusted input on the server. Client validation may mirror server rules for a better experience, but must not replace server enforcement.
- Use the project's established names and serialization conventions consistently. Avoid implicit transformations that make API payloads hard to trace.

## User flows and failures

- Represent loading, empty, success, and error states explicitly. Avoid effects that duplicate derived state or hide request lifecycle transitions.
- Map agreed server validation and error responses into clear, accessible UI feedback. Do not expose stack traces, internal exception text, or sensitive server details to the browser.
- Make retries, cancellation, duplicate submissions, and stale responses explicit for operations where they affect correctness.
- Use semantic HTML and accessible names; preserve keyboard operation, visible focus, understandable error feedback, and responsive reflow.

## Security and data handling

- Treat all browser state and requests as untrusted. Enforce authorization and resource ownership in ASP.NET Core for every protected operation.
- Follow the project's documented authentication model. Do not place credentials or long-lived secrets in browser storage or logs without an explicit, reviewed design.
- Minimize data returned to the UI and redact secrets, tokens, and unnecessary personal data from logs and error reporting.

## Changes and evidence

- Prefer vertical implementation slices that deliver a coherent behavior across API and UI; keep any required proof or compatibility experiment in Slice 1 of the spec.
- For each cross-stack change, identify focused server tests, UI/component tests, API contract or integration checks, and browser/end-to-end evidence that establish the behavior.
- Keep API contract updates, client types, and relevant examples synchronized in the same change when the repository owns them together.
- Before adding a dependency in either stack, follow the shared dependency agreement and review its maintenance, license/commercial terms, transitive risk, and vulnerability status.
