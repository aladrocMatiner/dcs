## File Layout (proposed)

Tutorial root:
- `docs/dcs-lua/README.md` (English)
- `docs/dcs-lua/README.es.md` (Español)
- `docs/dcs-lua/README.sv.md` (Svenska)
- `docs/dcs-lua/README.fi.md` (Suomi)

Chapter 01:
- `docs/dcs-lua/ch01.md`
- `docs/dcs-lua/ch01.es.md`
- `docs/dcs-lua/ch01.sv.md`
- `docs/dcs-lua/ch01.fi.md`

## Naming Conventions

- English uses the base filename (no `.en` suffix): `README.md`, `ch01.md`.
- Other languages use suffixes: `.es.md`, `.sv.md`, `.fi.md`.

## Navigation Conventions

- Each file starts with a single-line language bar:
  - Active language is bold and not linked.
  - Other languages link to the matching file name.
- `README*` contains a short index that links to the chapters in the same language.

## Chapter 01 Outline (DCS-only Lua, conceptual intro)

1. What DCS is (high level) and what a “mission” is in practice.
2. What Lua is (as a scripting language) and why DCS uses Lua for mission scripting (high level).
3. What mission scripting can do (conceptual examples):
   - Training cues and messaging
   - Reacting to events (takeoff/landing/kills) to drive flow
   - AI group activation/spawning and simple behavior control
   - State/flags for scoring and progression
   - Zones and timers (conceptual)
4. Where Lua runs in DCS:
   - Mission Editor triggers: `DO SCRIPT`, `DO SCRIPT FILE` (conceptual explanation; code comes later).
5. How to “test” scripts conceptually:
   - Verify execution, iterate, keep scope small.
6. Common mistakes:
   - Trigger not firing, typos, wrong names, expecting defaults, silent failures.
7. Next steps:
   - Chapter 02 focuses on first real code, smallest useful patterns, and a guided first script.

## Non-goals (Chapter 01)

- No MOOSE/MIST dependency.
- No code-heavy sections (only tiny snippets if strictly necessary; main value is the overview).
- No deep APIs that require verification in a running DCS environment.
- No keybind advice (unrelated to mission scripting).
