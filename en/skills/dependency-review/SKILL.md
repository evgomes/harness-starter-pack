---
name: dependency-review
description: Review project dependencies for inventory, license evidence, maintenance, known vulnerabilities, update opportunities, and documented risk. Use for dependency changes or the project's scheduled dependency review; this skill does not schedule itself.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Dependency review

## Start with project evidence

1. Read `docs/agreements/dependencies.md` and identify ecosystems, manifests, lockfiles, registries, policy, audit owner, and review cadence.
2. Inspect package manifests and lockfiles. Keep direct and transitive results distinct; do not infer resolved versions from version ranges.
3. Use the project's configured, approved package sources and security scanners. Record exact commands, tool versions, data sources, date, and scope.

## Assess each relevant package

- Purpose and whether it is still used.
- Resolved version, direct/transitive status, and supported maintenance/release status.
- License evidence from package metadata and the actual license text; note dual licenses and obligations for legal review.
- Known advisories, affected range, severity, reachability/exposure, available fixed versions, and source freshness.
- Update compatibility, breaking changes, transitive impact, and rollback options.

For ASP.NET Core, a candidate check is `dotnet package list --include-transitive --vulnerable`; for React/npm, a candidate check is `npm audit`. Verify the installed SDK/npm version, lockfile state, configured registries, and whether audit data is available before relying on results. `npm audit fix` changes the dependency tree; do not run it as a read-only audit.

## Report and update

Update `docs/agreements/dependencies.md` with verified inventory or findings, remediation/accepted-risk decision, owner, evidence link, and next review date. Classify proposals separately from approved updates. Never claim that “no vulnerabilities” means a dependency is secure; report scanner limitations and the data source.

## Periodic review

This skill only runs when invoked. For recurring checks, configure the repository's CI or scheduled automation to run approved deterministic scanners, produce a concise report, and route findings to an owner. Do not create an unapproved schedule, install tooling, publish reports externally, or upgrade packages automatically.
