---
name: dcs-kneeboard-builder
description: Create compact Digital Combat Simulator (DCS) kneeboard content (checklists, flows, radio presets, weapon employment notes) in Markdown-friendly formats with clear “do/check” steps. Use when asked to generate kneeboard pages, printable checklists, cockpit quick references, or to compress longer tutorials into cockpit-ready pages.
---

# DCS Kneeboard Builder

## Overview

Turn long procedures into cockpit-ready kneeboard pages: short, scannable, and consistent.

## Workflow

1. Confirm target.
   - Ask aircraft/module, scenario (cold start vs hot), and the intended use (training vs combat vs emergency).
2. Choose page type.
   - Use `references/kneeboard-patterns.md` templates (checklist / frequencies / weapons / nav).
3. Write in “Do / Check / Notes” format.
   - Keep each step atomic; avoid paragraphs.
4. Optimize for scan speed.
   - One page = one job; avoid mixing topics.
5. Provide export guidance.
   - Deliver Markdown source; optionally include a “how to render to image/PDF” suggestion if requested.

## Output Standard

- Prefer tables or short numbered lists.
- Use consistent terminology for switches (keep cockpit labels literal).
- If keybinds are mentioned, do not assume defaults; use “(bind)” placeholders.

## Resources

- Kneeboard templates and layout rules: `references/kneeboard-patterns.md`
