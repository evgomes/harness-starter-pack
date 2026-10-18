---
name: ui-design-exploration
description: Explore and prototype a user interface when the engineer wants help choosing a design direction before writing an implementation spec. Research at least three design ideas, build a mocked-data prototype with the target app stack and reusable design-system components, and hand the accepted direction into the spec workflow.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# UI design exploration

Use this optional skill when the engineer knows the user problem but wants to explore how a screen or interaction should look and work. Skip it when the design is already clear or the task is a direct implementation. This is a design exploration and prototype; do not silently turn it into production feature implementation.

## 1. Inspect the project and agree on the exploration boundary

1. Read repository instructions, design-system/styleguide guidance, accessibility target, stack profile, and relevant routes/components.
2. Identify the actual UI stack, tokens, component library, routing, and prototype/demo conventions from the repository. Reuse them; do not introduce a parallel design system or install dependencies without approval.
3. Confirm the task, target users, known requirements, constraints, affected screen/route, and what is explicitly not part of the prototype. Ask only questions whose answers could change the design or scope.
4. Before editing, follow repository branch rules and confirm the branch and working tree. If the work later transitions to a spec, retain a suitable branch or follow the repository's branch policy for that transition.
5. Keep backend/API integration out of the prototype unless explicitly requested. Use clearly identified mock data and avoid real personal or confidential data.

## 2. Research at least three design ideas

Research a minimum of three materially different ideas from current products, design systems, documented patterns, or reputable guidance. Use web research when available. Cite direct URLs and access dates, and record what design lesson each reference offers. Compare options against the project context instead of presenting a mood board without a decision. Do not copy a site's branding, proprietary assets, or distinctive layout wholesale.

Compare the options for:

- fit to the user goal and product context;
- interaction and information hierarchy;
- visual treatment and responsive behavior;
- implementation fit with the existing design system and stack;
- accessibility strengths and tradeoffs;
- risks, unanswered questions, and the smallest useful prototype.

The engineer chooses or adjusts the direction. Keep unaccepted concepts labeled as options, not requirements.

## 3. Plan the prototype

Use the shared [UI design exploration template](../../docs/templates/ui-design-exploration.md) and the applicable stack template. Identify:

- the route, screen states, viewport sizes, and interactions to demonstrate;
- the mock data shape and how it will be separated from real services;
- existing components to reuse and any new reusable components;
- every new or changed component's entry in the project's design system/styleguide;
- light and dark themes, system preference, contrast, and any project-supported theme customization;
- token names and override points for color, typography, spacing, radius, and other relevant properties;
- accessibility behavior to prototype and inspect, including keyboard, focus, semantics, and status/error announcements.

Treat end-user customization of colors, fonts, or other theme values as a product question, not an automatic feature requirement. Explore feasibility, accessibility safeguards, persistence, and user value; record whether the decision is prototype-only, a later option, or accepted scope.

## 4. Build and review the prototype

1. Implement the chosen prototype using the app's existing framework, styling approach, and design-system conventions.
2. Use mock data, realistic loading/empty/error states where relevant, and reusable components. Avoid hard-coded one-off styling where agreed tokens or overridable custom properties should be used.
3. Add or update the project's styleguide/design-system documentation for each reusable component introduced or materially changed. Document purpose, API/variants, states, semantic behavior, tokens, theme support, responsive behavior, and examples.
4. Demonstrate light and dark appearances. Where the project supports customization, demonstrate overrides without making inaccessible combinations easy to select. Check system theme behavior and contrast/focus states relevant to the screen.
5. Inspect the actual running prototype at target viewport sizes. Exercise keyboard interaction and important states. Load the `accessibility-review` skill and any relevant project design/accessibility skills; apply the project's WCAG target, and treat automated checks as a supplement to manual inspection.
6. Keep source changes limited to the prototype, reusable UI components, mock data, and styleguide/design-system entry. Do not wire production APIs, change unrelated screens, or claim final acceptance criteria have passed.

## 5. Capture decision and hand off to specification

Use the shared template and a handoff to record the implementation paths, mocked-data boundary, research references, design-system entries, accessibility observations, known limitations, and exact next step. Present the working prototype for engineer review. Record the selected direction and requested changes as human decisions.

When the engineer approves the design and wants to proceed, transfer the accepted behaviors, screen states, component contracts, accessibility requirements, and open questions into the shared or stack-specific feature spec. Follow the project branch-first spec workflow, get engineer review of acceptance criteria, and plan implementation slices. The prototype itself is not authorization to skip spec review or to treat mock behavior as production behavior.

## References

- [W3C Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C Understanding WCAG](https://www.w3.org/WAI/WCAG22/Understanding/)
