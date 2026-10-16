# React threat-model prompts

Use these prompts as an extension to the shared [threat-model template](../../../../docs/templates/threat-model.md), not as a replacement. Answer only what applies and verify details against the actual browser, server, rendering, and deployment architecture.

## Boundaries and components

- Which routes, components, browser storage, server-rendered pieces, API clients, and third-party scripts participate?
- Which data or operations cross from server to browser, browser to API, or application to external origin?
- What is public client code, and which controls remain authoritative on the server?
- Are server-side rendering, server actions, edge functions, or build-time environment variables in use?

## React/browser-specific threat prompts

- Could authentication or authorization rely only on hidden UI, route guards, client state, or disabled controls instead of server checks?
- Could personal data, tokens, API keys, or server-only configuration be bundled, serialized into HTML, or written to browser storage/logs?
- Can untrusted values reach HTML rendering, URL/navigation sinks, rich-text rendering, or unsafe DOM APIs?
- Are redirect destinations, links, iframe/embed sources, and external resource origins constrained where needed?
- Could stale requests, race conditions, caching, optimistic updates, or shared client state reveal another user's data?
- Are sensitive values exposed in errors, analytics, telemetry, source maps, URLs, or browser history?
- Could third-party scripts, dependencies, or compromised build inputs access sensitive page data?
- Do forms and client validation match server-side validation without being mistaken for an authorization or integrity boundary?
- Are CSRF, cookie, CORS, and token-storage assumptions based on the actual API and deployment topology?

For each applicable concern, describe a concrete actor/action/impact scenario and connect mitigations to server-side controls, tests, browser configuration, or deployment evidence. Client-side checks improve user experience but cannot enforce trust against a caller who controls the browser.
