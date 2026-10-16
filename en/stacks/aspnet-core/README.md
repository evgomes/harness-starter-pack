# ASP.NET Core profile

Backend guidance for projects built with ASP.NET Core. These recommendations are a starting point, not assumptions about every project: verify the repository, record accepted decisions in its agreements, and tailor them to the actual product.

## Use with other profiles

Select this profile for an ASP.NET Core backend. Add the [React profile](../react/README.md) independently when the project also uses React. Keep API/UI contracts and cross-stack decisions in the project's common `docs/agreements/architecture.md`.

## Architecture and conventions

- [Architecture profile](docs/agreements/architecture.md)
- [Conventions profile](docs/agreements/conventions.md)
- Keep the common [dependency agreement](../../docs/agreements/dependencies.md) current.
- Use the stack-specific [templates](docs/templates/README.md) for API/domain specifications, verification plans, and threat-model prompts.

## Candidate checks

Confirm commands against the installed SDK, solution, and CI configuration before using them:

| Area | Candidate checks |
|---|---|
| Formatting | `dotnet format --verify-no-changes` |
| Build | `dotnet build <solution-or-project>` |
| Tests | `dotnet test <solution-or-test-project>`; use focused tests during slices and run the required full suite at the end of spec implementation |
| Vulnerability audit | `dotnet package list --include-transitive --vulnerable` (confirm SDK and package-source audit support) |

The vulnerability listing reports against configured audit data; review source support and command output before interpreting an empty result. See [Microsoft's command reference](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-list).
