---
name: dcs-training-author
description: Write, translate, and refactor Digital Combat Simulator (DCS) documentation, tutorials, checklists, and course curricula in Markdown, using a professional instructor‑pilot voice, pedagogy‑first structure, and optional DCS Lua mission-scripting examples. Use when asked to create/update/translate DCS module docs (quick takeoff, beginner manuals, kneeboards), design training lessons/courses, standardize multi-language doc structure/links, or draft Lua snippets for DCS missions.
---

# DCS Training Author

## Overview

Produce beginner-friendly, structured DCS training content (docs, tutorials, and course material) and keep multi-language Markdown consistent, link-safe, and easy to follow.

## Workflow

1. Confirm scope and audience.
   - Ask: DCS module/aircraft, user level, `Game` vs `Sim`, input device (keyboard/mouse, HOTAS), and target language(s).
   - Ask: deliverable type (quick takeoff, lesson, course, reference), and whether to include mission scripting (Lua) or just procedures.
2. Choose a template and structure.
   - Use `references/doc-patterns.md` for ready-to-fill templates (quick takeoff / lesson / course).
3. Draft the content with “do → check → why (brief) → common mistakes → practice”.
4. Add controls guidance without inventing binds.
   - Never claim module-specific defaults; use a “(bind)” placeholder for anything that might be unbound or customized.
   - For common DCS defaults (e.g., `G` gear, `W` wheel brakes), label as “common default; verify”.
5. Keep links localized and relative.
   - If there are per-language files, link to the matching language version when it exists.
6. (Optional) Add Lua snippets as examples, not gospel.
   - Use `references/lua-patterns.md` and keep code minimal + testable; avoid relying on unverified APIs.
7. Validate links (optional but recommended).
   - Run `scripts/check_md_links.py` against the docs tree you touched.

## Output Standards

- Use short sections and explicit headings; prefer numbered steps for procedures.
- Always include:
  - Prerequisites / setup
  - Step-by-step sequence
  - Bindings checklist (with “(bind)” placeholders as needed)
  - “Mouse vs binds” note for cockpit interactions
  - Common mistakes + recovery
  - A short practice exercise (what to do next)

## Multi-language Rules

- Keep per-language docs structurally similar (same section order; localized prose).
- Use a single-line language bar at the top; bold the active language.
- Keep links in each language pointing to the matching language doc when available.

## Lua Guidance (DCS Missions)

- Only include Lua when asked (or when it materially improves the training).
- Prefer small, explainable scripts:
  - Event handler pattern
  - Simple triggers + messages
  - Small helper functions and logging
- If uncertain about an API name, say so and suggest the user verify in DCS scripting docs / Mission Editor environment.

## Resources

- Templates and patterns: `references/doc-patterns.md`
- Lua patterns and safe snippets: `references/lua-patterns.md`
- Markdown link checking: `scripts/check_md_links.py`
