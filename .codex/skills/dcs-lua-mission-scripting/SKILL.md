---
name: dcs-lua-mission-scripting
description: Write, debug, and refactor Digital Combat Simulator (DCS) mission scripting in Lua, including small event handlers, triggers, helper functions, and test plans. Use when asked for DCS Lua examples, Mission Editor scripting help, troubleshooting mission scripts, or when adding Lua snippets to DCS documentation/tutorials.
---

# DCS Lua Mission Scripting

## Overview

Produce minimal, readable Lua scripts for DCS missions, plus a concrete “how to test” checklist and safe debugging guidance.

## Workflow

1. Confirm constraints.
   - Ask which environment: Mission Editor `DO SCRIPT`, `DO SCRIPT FILE`, or server-side hooks.
   - Ask whether they use MIST/MOOSE or pure vanilla (default to vanilla).
   - Ask for goal + success condition (what should happen, for whom, and when).
2. Prefer Mission Editor triggers when they suffice.
   - If the request is simple (message on takeoff, set flag, activate group), offer ME triggers first.
3. If Lua is needed, start from a known-small pattern.
   - Use `references/patterns.md` and keep code focused on one responsibility.
4. Add debug output and a test plan.
   - Include at least one on-screen message and one log line suggestion.
5. Be explicit about uncertainty.
   - If an API name can’t be verified, label it and tell the user what to check in their DCS environment.

## Output Standard

- Put configuration first (zone/group names, message text).
- Keep scripts short; prefer one file / one handler.
- Include “How to install” (where to paste) + “How to test”.

## Resources

- Lua patterns + test checklists: `references/patterns.md`
