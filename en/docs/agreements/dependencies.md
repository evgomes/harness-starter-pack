# Dependency agreement

> Status: starter template. Keep the inventory current; never claim a license or security status without verifying its source.

## Policy

- Record direct and relevant transitive runtime/development packages, their resolved versions, purpose, and license.
- Check package health, license obligations, known vulnerabilities, update path, and transitive impact before adding or upgrading a package.
- Do not assume an SPDX identifier proves compliance; review the package's published license and any exceptions or dual licensing.
- Do not commit audit exports containing credentials, private registry URLs, or unnecessary environment data.
- Record the audit date, tools/data sources, unresolved risks, owner, and next review date.

## Inventory

| Ecosystem | Package | Resolved version | Direct/transitive | License (source) | Purpose | Owner / notes |
|---|---|---|---|---|---|---|
| `<NuGet/npm/etc.>` | `<package>` | `<version>` | `<direct or transitive>` | `<SPDX / URL>` | `<purpose>` | `<notes>` |

## Vulnerability and update log

| Date | Package/advisory | Severity and affected range | Decision/remediation | Evidence / issue | Owner |
|---|---|---|---|---|---|
| `<date>` | `<item>` | `<verified range>` | `<upgrade, mitigation, accepted risk with rationale>` | `<link or file>` | `<owner>` |

## Tooling

| Tool | Version | Purpose / install source | Last checked |
|---|---|---|---|
| `<Graphify, scanner, formatter, etc.>` | `<version>` | `<purpose and install source>` | `<date>` |

## Review cadence

- Pull request: audit dependency changes and update this file in the same change.
- Periodic: run the project's dependency and license checks at `<cadence>` using `<CI job, scheduled automation, or named owner>`.
- On a report: triage against reachability, affected versions, exploitability, available fixes, and business impact; document accepted risk with an owner and expiry/review date.

An agent skill can guide this review; it cannot provide periodic checks while no agent or scheduled job is running. Prefer CI or a scheduled repository automation for recurring reports.

## Additional review sources

| Tool/source | Version or URL | What it checks | Last used |
|---|---|---|---|
| `<registry / scanner / official advisory source>` | `<version/link>` | `<scope>` | `<date>` |
