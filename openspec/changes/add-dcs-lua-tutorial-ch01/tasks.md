## 1. Implementation

- [ ] 1.1 Create tutorial directory under `docs/dcs-lua/`
- [ ] 1.2 Add `README.md`, `README.es.md`, `README.sv.md`, `README.fi.md` with a localized language bar and a chapter index
- [ ] 1.3 Add Chapter 01 files in four languages:
  - [ ] `docs/dcs-lua/ch01.md`
  - [ ] `docs/dcs-lua/ch01.es.md`
  - [ ] `docs/dcs-lua/ch01.sv.md`
  - [ ] `docs/dcs-lua/ch01.fi.md`
- [ ] 1.4 Chapter 01 content (DCS-specific):
  - [ ] Explain where Lua runs in DCS (Mission Editor triggers: `DO SCRIPT`, `DO SCRIPT FILE`)
  - [ ] Show minimal patterns: `trigger.action.outText`, event handler skeleton
  - [ ] Add a “how to test” checklist and “common mistakes”
  - [ ] Do not invent module-specific keybind defaults (not relevant here; keep it DCS scripting-focused)
- [ ] 1.5 Validate:
  - [ ] Run `openspec validate add-dcs-lua-tutorial-ch01 --strict`
  - [ ] Ensure all internal Markdown links resolve (if any are added)
