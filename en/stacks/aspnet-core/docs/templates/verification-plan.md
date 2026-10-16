# ASP.NET Core verification plan: [change]

> Related specification: [link] · Owner: [name/team] · Target .NET / ASP.NET Core version: [verified version]

Use with the common [verification-plan template](../../../../docs/templates/verification-plan.md). Commands below are examples only; confirm the SDK, solution layout, package sources, test infrastructure, and scripts in the target repository. Do not claim a check passed unless it ran successfully.

Run focused checks for each active slice and record results in both this plan and the handoff before advancing. Defer the full test suite until all spec slices are complete unless the accepted spec or project agreement requires an earlier full run. Run one adversarial review at the end against the whole spec and final diff, using a strong model if available or having the engineer run the review skill manually.

## Change-specific evidence

| Requirement / invariant | Evidence required | Result / link | Status |
| --- | --- | --- | --- |
| API behavior and error contract |  |  | Not run |
| Authorization and data/tenant scope |  |  | Not run |
| Domain invariants |  |  | Not run |
| Persistence / migration behavior |  |  | Not run |

## Build and code checks

| Check | Candidate command or project entry point | Notes / result |
| --- | --- | --- |
| Formatting | `dotnet format <solution> --verify-no-changes` | Confirm SDK and formatting configuration. |
| Build | `dotnet build <solution-or-project>` | Record configuration and warnings/errors. |
| Static analysis | Project analyzers and configured rules | Record baseline and newly introduced findings. |
| Unit tests | `dotnet test <unit-test-project>` | Focus on domain/application behavior and invariants. |
| Integration tests | `dotnet test <integration-test-project>` | Verify real provider/hosting behavior where it matters; isolate test data. |
| API/contract tests | Project-specific test command | Include status codes, stable error identifiers, validation, and compatibility. |

## Data, security, and operations

| Concern | Evidence to collect | Result / link | Status |
| --- | --- | --- | --- |
| EF Core query shape, constraints, and transaction behavior | Relevant tests, SQL/query inspection, or migration review |  | Not run |
| Migration apply and rollback/forward-recovery | Migration review and disposable/test database evidence |  | Not run |
| Authentication, authorization, ownership/tenant isolation | Tests for allowed and denied access, including object scope |  | Not run |
| Input validation, output/error handling, and resource limits | Boundary tests and focused review |  | Not run |
| Secrets, configuration, logging, and personal data | Configuration review; verify redaction and safe defaults |  | Not run |
| Dependencies and known vulnerabilities | Project-approved audit command/source; record date and scope |  | Not run |
| Observability and failure behavior | Logs/metrics/traces and dependency failure evidence where relevant |  | Not run |

## Release and gaps

- Required checks from the project's [quality and security agreement](../../../../docs/agreements/quality-and-security.md):
- Checks not run, with reason:
- Environment assumptions and limitations:
- Migration/rollout owner and recovery plan:
- Risk exception link, if applicable:

Allowed status values: `Passed`, `Failed`, `Skipped`, `Not run`, or `Not applicable`.
