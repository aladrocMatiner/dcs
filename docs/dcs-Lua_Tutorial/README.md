# DCS Lua Tutorial

🇬🇧 **English** | 🇪🇸 [Español](README.es.md) | 🇸🇪 [Svenska](README.sv.md) | 🇫🇮 [Suomi](README.fi.md)

This tutorial focuses on **Lua mission scripting for DCS**, not aircraft avionics or modding. It is written to be practical, beginner-friendly, and progressively built chapter by chapter.

## How to use this tutorial (low frustration)

- Read one chapter and do its “Quick test” before moving on.
- Change **one thing at a time**.
- If something breaks, go back to the simplest version (one `outText`) and rebuild step by step.
- Save the mission every time you change triggers or scripts.

## How to run the examples in DCS (Mission Editor)

You can do it in two ways:

### Option A — `DO SCRIPT` (paste)

1) Mission Editor → *Triggers*
2) Trigger: `MISSION START`
3) Action: `DO SCRIPT`
4) Paste the chapter’s `lua` block.

### Option B — `DO SCRIPT FILE` (recommended)

1) Open the chapter and find its example file in [examples/](examples/).
2) Mission Editor → *Triggers*
3) Trigger: `MISSION START`
4) Action: `DO SCRIPT FILE`
5) Select the `.lua` file (for example `examples/ex03_hello.lua`).
6) Save the mission (DCS usually packs the script into the `.miz`).
7) Run the mission.

### How to “see results” (important)

- On screen: `trigger.action.outText("text", 10)`
- In logs: `env.info("message")` → `Saved Games\\DCS\\Logs\\dcs.log`

> If you get an error, start again from Chapter 03 and make sure your “heartbeat message” appears on screen.

## Safety / limits

The mission environment (MSE) is often **sanitized** for security. Some Lua libraries (`io`, `os`, `lfs`) may be disabled or restricted. This tutorial does not include instructions to change that.

## Chapters

- Chapter 01 — Introduction: DCS + Lua + what scripting enables: [ch01.md](ch01.md)
- Chapter 02 — Workflow pipeline (VS Code), setup, and common libraries: [ch02.md](ch02.md)
- Chapter 03 — Welcome (Cap 0): your first Lua win in DCS: [ch03.md](ch03.md)
- Chapter 04 — Where Lua runs in DCS (and where to paste it): [ch04.md](ch04.md)
- Chapter 05 — Variables (no fear): store mission data: [ch05.md](ch05.md)
- Chapter 06 — Strings and clean messages (`string.format`): [ch06.md](ch06.md)
- Chapter 07 — Tables as configuration (CFG): [ch07.md](ch07.md)
- Chapter 08 — If/Else + flags: simple decisions: [ch08.md](ch08.md)
- Chapter 09 — Functions: stop copy/paste: [ch09.md](ch09.md)
- Chapter 10 — Time + safe scheduler: [ch10.md](ch10.md)
- Chapter 11 — F10 menu: player controls: [ch11.md](ch11.md)
- Chapter 12 — Events: simple counter / scoreboard: [ch12.md](ch12.md)
- Chapter 13 — Script structure: `MyMission` + config + logic: [ch13.md](ch13.md)
- Chapter 14 — Debugging: practical checklist: [ch14.md](ch14.md)
- Chapter 15 — Copy/paste recipes: [ch15.md](ch15.md)
