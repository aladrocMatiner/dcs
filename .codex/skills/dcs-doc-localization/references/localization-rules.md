# DCS Doc Localization Rules (EN/ES/SV/FI)

## What to translate vs keep literal

Translate:
- Explanations, warnings, “why”, and recovery notes.
- Plain-language labels like “Step-by-step”, “Common mistakes”, “Practice”.

Keep literal (or keep the cockpit label + translate around it):
- Cockpit labels and abbreviations as printed in-cockpit (`NAV`, `BER`, `SPAK`, etc.).
- Units and numeric thresholds (unless converting units is explicitly requested).
- File names and relative link targets.

## Structure rules

- Keep the same headings in the same order across languages.
- Prefer 1:1 paragraph mapping (don’t add/remove large blocks unless asked).

## Link rules

- Use relative links.
- Localize links when a translated target exists:
  - Spanish file should link to `.es.md` target when present.
  - Swedish file should link to `.sv.md` target when present.
  - Finnish file should link to `.fi.md` target when present.
- If a translated target doesn’t exist, link to English and label it explicitly.

## Language bar rules

Use one single line near the top with the four languages:

`🇬🇧 **English** | 🇪🇸 [Español](README.es.md) | 🇸🇪 [Svenska](README.sv.md) | 🇫🇮 [Suomi](README.fi.md)`

Rules:
- Bold the active language label.
- Don’t link the active language to itself.
- Only link to files that exist (or create the missing files).

## Terminology consistency

- Maintain a small glossary for recurrent terms if you notice drift.
- Avoid “creative” synonyms for cockpit/systems concepts; keep consistent phrasing.
