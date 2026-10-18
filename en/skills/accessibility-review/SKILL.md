---
name: accessibility-review
description: Review UI changes against the project's accessibility agreement and applicable WCAG success criteria. Combine source review and approved automated checks with keyboard and assistive-technology evidence; do not claim conformance from automation alone.
metadata:
  version: "0.1.0"
  created: "2026-10-16"
---

# Accessibility review

1. Confirm the project's required accessibility standard, version, level, user groups, and any jurisdiction-specific requirements. If none is recorded, identify this as a project decision rather than silently asserting conformance.
2. Inspect changed UI and states for semantic structure, labels/names, keyboard operation, focus order/visibility/return, error identification and recovery, status announcements, contrast, text resizing/reflow, motion, target size, and alternatives to drag/gesture-only interactions.
3. Run the project's configured automated accessibility checks when appropriate. Record tool/version, pages/components, result, and known limitations.
4. Manually exercise affected flows with keyboard and relevant assistive technology when available. Record browser/AT, steps, expected/actual behavior, and any untested combinations.
5. Report concrete failures against the applicable criterion or project agreement, with scenario, impact, `path:line` or reproduction steps, and correction. Separate verified findings from risks that need user testing.

For web projects, consult the official [WCAG 2.2 recommendation](https://www.w3.org/TR/WCAG22/) and applicable project policy. WCAG includes normative success criteria; techniques and automated tools are aids, not proof of full conformance. Do not claim certification or legal compliance.
