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

- [Chapter 01](ch01.md) — Introduction: DCS + Lua + what scripting enables
- [Chapter 02](ch02.md) — Workflow pipeline (VS Code), setup, and common libraries
- [Chapter 03](ch03.md) — Welcome (Cap 0): your first Lua win in DCS
- [Chapter 04](ch04.md) — Where Lua runs in DCS (and where to paste it)
- [Chapter 05](ch05.md) — Variables (no fear): store mission data
- [Chapter 06](ch06.md) — Strings and clean messages (`string.format`)
- [Chapter 07](ch07.md) — Tables as configuration (CFG)
- [Chapter 08](ch08.md) — If/Else + flags: simple decisions
- [Chapter 09](ch09.md) — Functions: stop copy/paste
- [Chapter 10](ch10.md) — Time + safe scheduler
- [Chapter 11](ch11.md) — F10 menu: player controls
- [Chapter 12](ch12.md) — Events: simple counter / scoreboard
- [Chapter 13](ch13.md) — Script structure: `MyMission` + config + logic
- [Chapter 14](ch14.md) — Debugging: practical checklist
- [Chapter 15](ch15.md) — Copy/paste recipes
