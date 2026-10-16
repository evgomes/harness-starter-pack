# Engineering conventions

> Status: starter template. Keep project-specific choices explicit; avoid copying rules that do not fit the codebase.

## SOLID and design

- **Single Responsibility:** give a module one cohesive reason to change; avoid splitting code into tiny units without a real boundary.
- **Open/Closed:** extend through a stable abstraction when variants are expected; do not create speculative extension points.
- **Liskov Substitution:** implementations must preserve the behavioral contract of their abstractions.
- **Interface Segregation:** keep contracts focused on the needs of their consumers.
- **Dependency Inversion:** keep high-level policy independent of replaceable infrastructure where that boundary provides practical value.

Apply these principles with judgment. Prefer the simplest design that keeps responsibilities clear and changes testable.

## Clean Code

- Use names that communicate domain intent; keep functions cohesive and control flow easy to follow.
- Make invalid states difficult to represent and validate inputs at system boundaries.
- Avoid hidden side effects, duplicated rules, unnecessary indirection, and comments that restate the code.
- Handle errors explicitly; do not swallow failures or catch broadly without a recovery/translation reason.
- Keep code and tests aligned with existing repository patterns unless changing a pattern is part of the agreed work.

## Project-specific conventions

| Topic | Agreed convention | Rationale / evidence |
|---|---|---|
| Naming and formatting | `<rules and formatter>` | `<source>` |
| Error handling | `<contract>` | `<source>` |
| Logging/observability | `<fields, levels, redaction>` | `<source>` |
| Testing | `<test strategy and naming>` | `<source>` |
| API/UI/data contracts | `<rules>` | `<source>` |

## Security, privacy, accessibility

Address applicable OWASP guidance and the project threat model. For web UI, use the agreed WCAG target and combine automated tools with keyboard and assistive-technology checks. Minimize personal data; document jurisdiction-specific obligations with the organization's privacy/legal owners. Generic guidance is not a compliance determination.
