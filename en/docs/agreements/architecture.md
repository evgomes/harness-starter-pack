# Architecture agreement

> Status: starter template. Replace every prompt with facts verified in this repository.

## Purpose and scope

- Product/system purpose: `<what the system does>`
- Users and primary workflows: `<who uses it and how>`
- Out of scope: `<explicit exclusions>`

## Technology stack

| Area | Technology and version policy | Evidence / location |
|---|---|---|
| Backend/API | `<framework, runtime, key packages>` | `<solution/project files>` |
| Frontend | `<framework, language, build system>` | `<package manifest/config>` |
| Data | `<database, persistence, migrations>` | `<configuration/schema>` |
| Hosting/deployment | `<runtime, containers, cloud/on-prem>` | `<deployment files>` |
| Tests and quality | `<test, lint, analysis tools>` | `<project scripts/config>` |

## Architecture contract

Describe the components, their responsibilities, and allowed dependency direction. Include a diagram or link when useful. Record boundaries that must remain true, not a generic list of patterns.

- `<component>` owns `<responsibility>`.
- `<component>` may depend on `<boundary>`; it must not depend on `<boundary>`.
- Public interfaces/contracts are defined in `<location>`.
- Data ownership, transaction boundaries, and migration policy: `<decision>`.
- Authentication, authorization, tenant/data isolation: `<decision>`.

## Quality attributes and constraints

Record relevant targets and decisions for availability, performance, scalability, observability, accessibility, privacy, security, compatibility, and deployment. Mark unresolved items as open questions rather than inventing targets.

## Change process

Architecture changes require a brief rationale, alternatives considered, affected contracts, migration/rollout implications, and an update to this agreement when the accepted design changes.
