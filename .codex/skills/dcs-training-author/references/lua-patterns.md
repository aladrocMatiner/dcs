# DCS Lua Patterns (Mission Scripting)

Keep Lua snippets short, testable, and clearly labeled as “example patterns”. If unsure about an API name, say so and ask the user to verify in their DCS environment.

## Minimal Event Handler Skeleton

```lua
local handler = {}

function handler:onEvent(event)
  if not event then return end
  if event.id == world.event.S_EVENT_TAKEOFF then
    trigger.action.outText("Takeoff detected", 5)
  end
end

world.addEventHandler(handler)
```

Notes:
- Prefer `trigger.action.outText(...)` for quick feedback while testing.
- Use `env.info("message")` for logging when troubleshooting.

## Safe Helper Style

```lua
local function safeName(unit)
  if not unit or not unit.getName then return "<nil>" end
  local ok, name = pcall(unit.getName, unit)
  return ok and name or "<err>"
end
```

## Simple “Zone Enter” Concept

Often easiest is to do zone logic in the Mission Editor, but if scripting is requested:
- Get zone by name (verify availability in your environment).
- Sample a unit’s position periodically and test if inside the zone.

(Keep implementation minimal; prefer pseudocode if you cannot verify the exact API calls.)

## Quality Bar for Lua in Training Docs

- Explain what the script does in 2–3 bullets before code.
- Put configuration at the top (zone name, group name, message text).
- Add a “How to test in DCS” checklist:
  - Where to paste (mission script / do-script trigger)
  - What to look for (on-screen text, log lines)
  - One known failure mode + fix (typo in zone name, missing group)
