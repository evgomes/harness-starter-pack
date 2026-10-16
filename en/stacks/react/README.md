# React profile

Frontend guidance for projects built with React. These recommendations are a starting point, not assumptions about every repository: verify its package manifests, framework configuration, tests, accessibility needs, and deployment model before adopting them.

## Use with other profiles

Select this profile for a React application or user interface. Add the [ASP.NET Core profile](../aspnet-core/README.md) independently when that backend is also present. Keep API/UI contracts, authentication boundaries, and cross-stack decisions in the project's common `docs/agreements/architecture.md`.

## Architecture and conventions

- Keep UI components focused on rendering and interaction; place reusable domain behavior in explicit modules when that improves testability and clarity.
- Keep server-owned authorization and validation authoritative. Treat browser code, route guards, and client-side validation as untrusted convenience controls.
- Represent loading, empty, success, and error states explicitly. Avoid hidden state coupling and effects that duplicate derived state.
- Use semantic HTML and accessible names; preserve keyboard operation, visible focus, understandable errors, and responsive reflow.
- Record the selected React version, rendering strategy, routing, state management, API client, and test approach in the project's architecture agreement.
- Use the stack-specific [templates](docs/templates/README.md) for UI specifications, verification plans, and browser/client threat-model prompts.
- Use the optional [UI design exploration skill](../../skills/ui-design-exploration/SKILL.md) and [React design templates](docs/templates/design-exploration.md) when comparing screen directions before spec creation. Prototype with mocked data, the app's existing stack, and reusable components documented in its design system.
- For browser-visible UI changes, use the optional [browser visual validation skill](../../skills/browser-visual-validation/SKILL.md) and prefer branded Chrome when available. The [cross-harness browser guide](../../guides/browser-testing.md) explains setup choices and how to report embedded-browser fallbacks accurately.

## Candidate checks

Derive actual commands from the repository's package scripts and lockfile; do not assume a package manager or install new tools as part of this profile.

| Area | Candidate checks |
|---|---|
| Formatting and lint | Existing formatter/linter scripts, scoped to changed files where supported |
| Type validation | Project typecheck script when TypeScript is used |
| Build | Production build script and configured environment |
| Tests | Focused component/unit tests during slices, then required full and integration/end-to-end checks at the end of spec implementation |
| Accessibility | Automated checks plus keyboard, focus, zoom/reflow, and assistive-technology checks appropriate to the change |
| Security | Review browser/server trust boundaries, sensitive data exposure, dependency changes, and configured source-analysis results |

Record chosen checks and required evidence in the project's [quality and security agreement](../../docs/agreements/quality-and-security.md) and use a [verification plan](../../docs/templates/verification-plan.md) for changes with cross-layer or elevated risk.
