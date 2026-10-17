# Stack profiles

Stack profiles add technology-specific architecture, conventions, and verification guidance to the shared agreements. They are suggestions until verified against a target project's manifests, source, and deployment configuration.

## Available

- [ASP.NET Core](aspnet-core/README.md)
- [React](react/README.md)
- [ASP.NET Core + React in one repository](aspnet-core-react/README.md)

Use the combined profile when an ASP.NET Core backend and React frontend live in the same repository and need shared architecture, conventions, and end-to-end spec guidance. Selecting it in the installer also includes both individual profiles for their technology-specific guidance. Use individual profiles when you want only one stack's guidance.

## Adding a profile

1. Create `stacks/<stack-name>/README.md` with scope, supported variants, prerequisites, and candidate checks.
2. Add only the architecture and convention extensions that differ from the common agreements.
3. Document lint, build, test, security, and accessibility commands as candidates and tie each to evidence/configuration; do not invent version pins.
4. Add focused skills only when a repeatable stack-specific workflow benefits from them.
5. Update this catalog and the root English README. Keep language-specific content inside its language package.
