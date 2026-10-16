# ASP.NET Core architecture profile

> Verify this profile against the target project before adopting. Record actual framework/runtime versions and architecture in its common `docs/agreements/architecture.md`.

## Responsibilities and boundaries

Document the API host, endpoint/transport boundary, application/domain rules, persistence, external integrations, background services, and composition root. State which layer owns each decision and the permitted dependency direction.

### Minimal APIs and resource grouping

When using Minimal APIs, group routes by resource in readable endpoint modules. Keep each request handler focused on boundary validation, invoking application/domain behavior, and mapping the result to the transport response. Business rules belong in domain/application types that can be tested without HTTP.

### Persistence boundary

EF Core owns database access and mapping. Keep query expressions in the persistence/data boundary; do not let `IQueryable` leak into domain or presentation logic. Make migration ownership, transaction boundaries, and database constraints explicit. Treat migrations as reviewed code; add a migration rather than rewriting one that has already been applied.

## Data and domain contracts

- Document each domain type in the product's language. Property documentation should explain domain meaning, invariants, mutability, and null semantics where these are not clear from the type/name.
- Avoid sentinel values and unexplained literals when they encode domain state. Use a named type, enum, or constant when it makes the state or rule explicit.
- Decide entity identity, timestamp ownership, UTC serialization, tenancy/ownership, and uniqueness scopes when the data model is agreed.
- Specify validation, compatibility, error format, and stable machine-readable error identifiers at API boundaries.

## Queries and performance

Shape reads to the data a use case needs. Avoid N+1 access patterns, unbounded materialization, and tracking for read-only queries where the chosen EF Core pattern supports no-tracking. Record pagination and query bounds for collections that can grow.

## Security and operations

Document authentication/authorization, data/tenant scoping, secret storage, allowed origins, request limits, logging/redaction, health and readiness behavior, and observability. For persisted identity or tenant scopes, define uniqueness and read/write isolation rules before implementation.

## Evidence and exceptions

Use the actual `.sln`/`.csproj`, API maps, service registration, EF model, migrations, tests, configuration, and deployment files as evidence. Keep implementation exceptions narrow and explain their tradeoffs in the project's agreements or a decision record.
