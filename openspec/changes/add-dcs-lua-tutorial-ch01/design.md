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

## Chapter 01 Outline (DCS-only Lua)

1. What DCS Lua scripting is (mission scripting, not cockpit avionics code).
2. Where Lua runs:
   - Mission Editor triggers: `DO SCRIPT`, `DO SCRIPT FILE`.
3. Minimal “hello world”:
   - `trigger.action.outText("...", seconds)`
4. Minimal event handler pattern:
   - Detect takeoff event and print a message.
5. How to test:
   - Add trigger, start mission, observe output, iterate.
6. Common mistakes:
   - Trigger not firing, typos in function names, silent failures, wrong scope.
7. Next steps:
   - Suggest Chapter 02 topics (e.g., zones, flags, simple state machines).

## Non-goals (Chapter 01)

- No MOOSE/MIST dependency.
- No deep APIs that require verification in a running DCS environment.
- No keybind advice (unrelated to scripting).
