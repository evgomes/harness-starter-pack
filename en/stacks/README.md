# Stack profiles

Stack profiles add technology-specific architecture, conventions, and verification guidance to the shared agreements. They are suggestions until verified against a target project's manifests, source, and deployment configuration.

## Available

- [ASP.NET Core](aspnet-core/README.md)
- [React](react/README.md)

Select profiles independently. For a full-stack ASP.NET Core + React application, apply both and record their API contract and integration decisions in the project's shared agreements.

## Adding a profile

1. Create `stacks/<stack-name>/README.md` with scope, supported variants, prerequisites, and candidate checks.
2. Add only the architecture and convention extensions that differ from the common agreements.
3. Document lint, build, test, security, and accessibility commands as candidates and tie each to evidence/configuration; do not invent version pins.
4. Add focused skills only when a repeatable stack-specific workflow benefits from them.
5. Update this catalog and the root English README. Keep language-specific content inside its language package.
