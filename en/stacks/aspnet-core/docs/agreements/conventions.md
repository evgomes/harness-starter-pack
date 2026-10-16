# ASP.NET Core conventions profile

> These are suggested defaults; keep only the conventions that fit the target project and record accepted decisions in its common agreements.

## Naming and code shape

- Prefer complete domain words over abbreviations (`request`, `response`, `cancellationToken`). Keep established domain terms and standard framework initialisms where they are clearer.
- Name types for their domain responsibility rather than an implementation pattern when that improves the shared vocabulary.
- Keep endpoint handlers small: validate boundary input, invoke the appropriate behavior, and map output. Move business decisions into domain/application logic.
- Apply SOLID to keep responsibilities cohesive and dependencies deliberate. Avoid adding abstractions, layers, or generic frameworks without a demonstrated change or testing benefit.
- Do not hide domain state in magic numbers, strings, or booleans. Use explicit types and names when a literal carries meaning.

## Async, cancellation, persistence

- Use asynchronous APIs for asynchronous I/O and accept/pass a `CancellationToken` through request-scoped asynchronous operations when supported.
- Keep EF Core queries inside the persistence boundary; do not return `IQueryable` to business or UI layers.
- Shape queries for the use case, project only required fields, avoid database work inside data-driven loops, and bound results that can grow.
- Use no-tracking reads when data is not modified and that matches the chosen query shape.
- Treat applied migrations as immutable history; add a new migration for schema changes.
- Centralize timestamp ownership and store/serialize instants in UTC when that is the project contract. Record the chosen identifier and tenancy/ownership strategy instead of assuming a universal one.

## Errors and logging

- A failed operation should have a failure response, not a successful status carrying a failure flag. Use the project's agreed HTTP error contract and stable machine-readable identifiers where clients branch on error types.
- Let centralized handlers own unexpected exceptions. A local catch should recover, translate a known external failure, or add context needed for one of those; avoid catch-log-rethrow, silent catches, and broad catches that mask defects.
- Use structured logging with stable fields. Log only context needed to operate and diagnose the system; redact credentials, tokens, connection strings, key material, and unnecessary personal data.
- Record handled degradation or fallback when an operator would otherwise be unable to explain a partial or misleading result.

## Reflection and dynamic behavior

Prefer explicit types, interfaces, switches over closed sets, and registered factories for business behavior. Use reflection only where a framework integration or a shape-based guard test justifies it, and document the reason because it is harder to find and verify statically.

## Tests and packages

- Test business behavior and meaningful invariants rather than framework plumbing. Name tests for the behavior they establish.
- Never disable or weaken a test merely to make a build pass. An environment-dependent skip must check a real runtime condition and explain how to enable the test.
- Use integration tests when the rule itself depends on the real database/provider/runtime; isolate their data and environment from development resources.
- Prefer platform/framework capabilities before adding packages. Before adding a dependency, verify purpose, maintenance, license/commercial terms, transitive risk, and vulnerability status; update `docs/agreements/dependencies.md` in the same change.
