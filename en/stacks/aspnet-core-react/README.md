# ASP.NET Core + React profile

Use this profile when the ASP.NET Core backend and React frontend are maintained in the same repository and a change may cross their boundary. It adds integrated architecture and convention guidance plus full-stack specification and verification templates. Selecting it in the installer also includes the standalone ASP.NET Core and React profiles for their technology-specific guidance. It does not generate an application or install framework dependencies.

The installer places this profile under `stacks/aspnet-core-react/`. Select it instead of selecting the individual ASP.NET Core and React profiles separately; the installer includes those individual profiles alongside this one. The combined profile focuses on decisions shared across the API and UI; verify all guidance against the actual project before adopting it.

## Agreements

- [Integrated architecture prompts](docs/agreements/architecture.md) for API/UI contracts, trust boundaries, data ownership, and deployment seams.
- [Integrated conventions](docs/agreements/conventions.md) for changes that span backend and frontend.
- Keep the project's shared [architecture agreement](../../docs/agreements/architecture.md), [conventions agreement](../../docs/agreements/conventions.md), [dependency agreement](../../docs/agreements/dependencies.md), and [quality and security agreement](../../docs/agreements/quality-and-security.md) authoritative and current.

## Templates

- [Full-stack feature specification](docs/templates/spec.md) for user-visible changes that cross the API/UI boundary.
- [Full-stack verification plan](docs/templates/verification-plan.md) for backend, frontend, contract, and end-to-end evidence.
- Use the common [specification](../../docs/templates/spec.md), [verification plan](../../docs/templates/verification-plan.md), and [threat model](../../docs/templates/threat-model.md) when their general structure fits better.

## Candidate checks

Choose commands from the repository's actual solution, package manifests, scripts, CI, and deployment configuration. Typical evidence may include a .NET build and focused tests, frontend type/lint/build and component tests, API contract checks, and a focused browser or end-to-end flow. Do not assume a package manager, framework version, or test tool from this profile alone.
