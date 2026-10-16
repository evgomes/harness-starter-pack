# React UI design exploration: [screen or feature]

> Status: Exploring / Prototype ready / Direction accepted / Handed off to spec · Owner: [engineer/designer] · Date: [date] · Branch: [repository-compliant branch]

Use with the shared [UI design exploration template](../../../../docs/templates/ui-design-exploration.md). Verify the repository's actual React version, rendering framework, router, design system, CSS approach, and scripts. The prototype should use this app's stack and existing conventions rather than introducing a parallel setup.

## Research and direction

- Shared exploration link (include at least three researched ideas with URLs and access dates):
- Selected option and engineer decision:
- User goal and target route/screen:
- Screen states: loading / empty / populated / error / disabled / success / other:
- Responsive breakpoints/viewports and interaction model:

## React prototype contract

- Existing route or isolated preview entry point:
- Component tree and responsibilities:
- Reusable components to create or change:
- Existing design-system components/tokens to reuse:
- Mock data module/types and reset mechanism:
- Network/API calls explicitly excluded from prototype:
- Framework-specific rendering or hydration considerations:
- Run/preview command from the repository's existing scripts:

Keep mock data visibly separate from production services. Do not add dependencies or modify production API behavior for a design exploration unless the engineer explicitly asks.

## Styling and theme contract

- Existing CSS strategy (CSS modules, stylesheets, utility classes, CSS-in-JS, etc.):
- Existing token source and naming convention:
- Override layer/mechanism that fits the app (for example, CSS custom properties if already suitable):
- Component-level values that should reference tokens rather than literals:
- Light theme values/states to demonstrate:
- Dark theme values/states to demonstrate:
- System preference and theme switch behavior:
- Potential user customization: color / font / density / other:
- Customization decision: exclude / demonstrate only / accepted requirement / future option:
- Persistence and reset behavior if customization is accepted:
- Guardrails: contrast, focus visibility, reduced motion, forced colors, and readable fallbacks:

Do not assume that end-user theme customization is in scope. If accepted, ensure overrides remain discoverable, testable, and resistant to inaccessible combinations.

## Accessibility and interaction review

- Relevant project WCAG target and success criteria:
- Semantic elements, accessible names, labels, and error relationships:
- Keyboard operation, focus order, focus return, and visible focus:
- Loading/error/status announcements:
- Contrast, zoom/reflow, target size, and motion considerations:
- Manual browser/keyboard checks and automated checks performed:
- Untested assistive technology/device combinations and limitations:

## Design-system/styleguide record

For every new or materially changed reusable component, complete [the component entry template](component-styleguide-entry.md) and add it to the project's actual design-system/styleguide location.

| Component | Responsibility / variants | Implementation path | Styleguide entry path | Status |
|---|---|---|---|---|
|  |  |  |  | Planned |

## Approval and spec transition

- Prototype preview / route:
- Mocked states shown:
- Engineer-selected direction and approval date:
- Requested changes / outstanding design decisions:
- Behaviors, states, component API, theme behavior, and accessibility criteria to move into the spec:
- Next action: create or update a feature spec on the repository-compliant branch; engineer reviews acceptance criteria before implementation.
