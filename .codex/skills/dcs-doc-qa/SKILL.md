---
name: dcs-doc-qa
description: "Quality-assure Digital Combat Simulator (DCS) Markdown documentation: validate relative links, enforce basic structure (headings like step-by-step/bindings/common mistakes), and produce actionable QA reports. Use when asked to review DCS docs for consistency, fix broken links, standardize headings, or run automated checks across a docs tree."
---

# DCS Doc QA

## Overview

Catch broken links and structural regressions in DCS docs and produce a short, fix-first report.

## Workflow

1. Decide the scope.
   - Single file vs a docs directory; whether multi-language checks are expected.
2. Run automated checks first.
   - Links: `scripts/check_md_links.py <root>`
   - Structure: `scripts/check_doc_structure.py <root> --preset quick-takeoff` (or custom `--require-regex`).
3. Fix issues in priority order.
   - Broken links → missing headings → inconsistent naming → style nits.
4. Re-run checks until clean.
5. Summarize changes as a short QA report.
   - What was broken, what was fixed, what remains (if any).

## Resources

- QA checklist: `references/qa-checklist.md`
- Link checker: `scripts/check_md_links.py`
- Heading/structure checker: `scripts/check_doc_structure.py`
