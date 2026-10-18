---
name: hook-authoring
description: Design, implement, or review an optional repository or harness lifecycle hook with explicit behavior, safe defaults, cross-platform support, and verifiable failure modes. Use when a project asks to add or change a hook.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Hook authoring

Hooks are optional integrations, not a universal mechanism. Keep the check itself portable where practical, then add a thin harness-specific adapter only when that harness supports the required event safely.

## Design

1. Read the project's quality and security agreement, existing hook configuration, and [hook guidance](../../hooks/README.md).
2. Confirm the need for a hook. Prefer an explicit skill/instruction for contextual reasoning, a local hook for fast deterministic checks, and CI or scheduled automation for authoritative or recurring checks.
3. Fill in `docs/templates/hook-contract.md`. Define the trigger, inputs, effects, runtime, operating systems, timeout, output, missing-prerequisite and error behavior, data/network use, disable path, manual command, and CI counterpart.
4. Check the target harness's current official documentation for event names, payloads, permissions, trust prompts, configuration, and version compatibility. Do not infer behavior from another harness.

## Implement and validate

1. Keep the core check focused, bounded, and idempotent. Make side effects explicit. Do not silently install dependencies, rewrite source, send code to a service, or weaken security settings.
2. Add only the required harness adapter and preserve existing project configuration. Include a clear opt-in, disable, and removal path.
3. Validate success, detected finding, missing prerequisite, timeout, and internal-error behavior on each supported operating system/runtime. Use a safe fixture or isolated sample repository where possible.
4. Document exact setup, command, expected output, requirements, limitations, and evidence. Update the contract and hook catalog when behavior changes.
5. Review the hook as code: quote paths safely, avoid leaking environment variables or secrets, constrain file/process/network access, and ensure failures are actionable without causing destructive behavior.

Do not claim cross-platform support unless the implementation has been checked on the stated platforms. If a platform could not be exercised, state that limitation and provide a manual verification step.
