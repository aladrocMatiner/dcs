## Dependencies

- Chapter 02 assumes the tutorial root (`docs/dcs-Lua_Tutorial/README*`) and Chapter 01 exist (from change `add-dcs-lua-tutorial-ch01`).

## File Layout (proposed)

Chapter 02:
- `docs/dcs-Lua_Tutorial/ch02.md`
- `docs/dcs-Lua_Tutorial/ch02.es.md`
- `docs/dcs-Lua_Tutorial/ch02.sv.md`
- `docs/dcs-Lua_Tutorial/ch02.fi.md`

## Chapter 02 Outline

1. The workflow pipeline (high level)
   - Edit in VS Code → package into mission → run in DCS → verify → iterate
2. What you do and don’t need to “install”
   - DCS runs Lua internally
   - Local tooling is for authoring (syntax checking, autocomplete, formatting), not required for execution
3. VS Code setup
   - Lua language server extension (diagnostics + completion)
   - Formatting conventions (keep changes small; consistent indentation)
   - Suggested folders (scripts/, libs/, notes/, missions/)
4. Built-in DCS API vs third-party libraries
   - Built-in: triggers/events/timers/messages
   - Third-party: abstractions and helpers
5. Common community libraries/frameworks (conceptual)
   - MIST: utility helpers + common patterns
   - MOOSE: framework for complex mission logic
   - Other popular add-ons (brief): IADS, logistics, admin/tools
6. When to use libraries vs Mission Editor triggers
   - Complexity threshold and maintenance trade-offs
7. Checklist: “my pipeline is ready”
   - VS Code configured
   - File organization chosen
   - Plan for adding scripts to mission decided
   - First “hello world” test plan ready (code comes in Chapter 03)

## Non-goals (Chapter 02)

- Not a code tutorial yet (no heavy code blocks).
- Not an endorsement of any specific library/version; keep guidance general.
