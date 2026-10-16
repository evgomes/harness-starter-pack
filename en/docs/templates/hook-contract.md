# Hook contract: [hook name]

Use this template to design an optional local or harness hook. It is a vendor-neutral planning document, not a universal hook configuration format. Translate the agreed behavior into the selected harness's current documented interface.

## Ownership and support

- Status: Proposed / Active / Retired
- Purpose and owner:
- Supported harnesses and versions:
- Official documentation checked on:
- Related [quality and security agreement](../agreements/quality-and-security.md):

## Behavior

- Trigger and conditions:
- Inputs available to the hook:
- Intended action and scope:
- Explicitly out of scope:
- Manual command for the same check:
- CI or other authoritative counterpart:

## Runtime contract

- Runtime and required version:
- Supported operating systems:
- Timeout:
- Exit statuses and user-facing messages:
- Output format and where diagnostics point:
- Behavior when a prerequisite is missing:
- Behavior on timeout or internal error:

## Safety and reliability

- Side effects (files, processes, network, repository state):
- Whether the operation is idempotent:
- Concurrency / repeated invocation behavior:
- Data sent or retained:
- Secrets required and how they are protected:
- Setup, installation, update, and removal instructions:
- Disable or bypass behavior and its limitations:

## Validation and adoption

- How behavior is validated on each supported OS:
- Expected behavior for success, finding, missing prerequisite, and failure:
- Configuration merge and user trust requirements:
- Rollback / removal steps:
- Known limitations:

Confirm the harness-specific event names, input schema, permissions, and configuration behavior against its official documentation before implementing. Do not assume hooks share a schema or that installing a hook framework is appropriate for every repository.
