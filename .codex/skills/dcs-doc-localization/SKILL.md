---
name: dcs-doc-localization
description: Localize and maintain multi-language Digital Combat Simulator (DCS) documentation in Markdown (EN/ES/SV/FI), keeping structure consistent, links localized, and terminology stable. Use when asked to translate DCS docs, add new languages, fix language bars/links, or standardize terminology across multiple DCS documents.
---

# DCS Doc Localization

## Overview

Translate and maintain DCS docs across languages without breaking navigation, structure, or cockpit terminology.

## Workflow

1. Inventory what exists.
   - Identify the “base name” docs set (e.g., `README.md`, `README.es.md`, `README.sv.md`, `README.fi.md`).
2. Establish translation rules.
   - Use `references/localization-rules.md`.
3. Keep structure identical.
   - Same headings/order; translate only prose.
4. Keep links localized.
   - In each language file, link to the matching language target when it exists.
5. Keep cockpit labels stable.
   - Don’t translate switch labels/abbreviations printed in-cockpit (e.g., `NAV`, `SPAK`, panel markings).
6. Validate.
   - Run `scripts/check_language_bars.py` after edits.

## Resources

- Localization rules + language bar conventions: `references/localization-rules.md`
- Glossary template (optional): `references/glossary-template.md`
- Automated checks: `scripts/check_language_bars.py`
