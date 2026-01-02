# DCS Lua Mission Scripting Patterns

Use these as *example patterns*; keep scripts small and add a test plan. If you cannot verify an API name, say so and tell the user what to check in their DCS environment.

## Minimal Event Handler

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

Test:
- Add via Mission Editor trigger: `MISSION START` → `DO SCRIPT`.
- Launch mission and take off.
- Expect on-screen message.

## Debugging Checklist

- Add a short on-screen message to prove code executed.
- Add `env.info("...")` log lines for deeper info.
- Confirm names match exactly (zone name, group name, unit name).
- Reduce scope: test with one unit/group first.

## Safe Helper Functions

```lua
local function safeCall(fn, ...)
  local ok, result = pcall(fn, ...)
  if not ok then
    env.info("Lua error: " .. tostring(result))
    return nil
  end
  return result
end
```

## Configuration-First Style

```lua
local CFG = {
  zoneName = "TRAINING_ZONE",
  message = "Entered zone",
  seconds = 5,
}
```

## When to Avoid Lua

Prefer Mission Editor triggers when:
- You only need: activate group, message, set flag, AI task push.
- The behavior is purely time/zone based without complex logic.
