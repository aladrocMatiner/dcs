# Cookbook — Mission Editor recipes (no Lua)

🇬🇧 **English** | 🇪🇸 [Español](cookbook.es.md) | 🇸🇪 [Svenska](cookbook.sv.md) | 🇫🇮 [Suomi](cookbook.fi.md)

Back to index: [README.md](README.md)

Each recipe is: **Goal → Ingredients → Steps → Quick test → Common errors**.

## Recipe 01 — Message when entering a zone

- **Goal**: teach the player “you are in the training area”.
- **Ingredients**: a trigger zone + one trigger.
- **Steps**:
  1. Create zone `ZONE_TRAINING`
  2. Trigger: condition “player in zone”
  3. Action: message “Entered training area”
- **Quick test**: fly into the zone, see the message once.
- **Common errors**: message spam → add a flag gate.

## Recipe 02 — Late-activated convoy starts on demand

- **Goal**: reduce load until needed.
- **Ingredients**: ground group `RED_CONVOY_01` with Late Activation.
- **Steps**:
  1. Mark convoy as Late Activation
  2. Trigger condition: time > 60s (or player in zone)
  3. Action: Activate group `RED_CONVOY_01`
- **Quick test**: convoy appears only after the trigger.
- **Common errors**: wrong group name → re-check group ID/name.

## Recipe 03 — Three-phase mission using flags

- **Goal**: clean mission flow without spaghetti triggers.
- **Ingredients**: flags `10` (started), `20` (objective complete).
- **Steps**:
  1. F10 menu “Start exercise” → set flag `10 = 1`
  2. Enter zone trigger only if flag `10 == 1`
  3. Objective completion sets flag `20 = 1` and shows “RTB”
- **Quick test**: nothing happens before start; phases happen in order.
- **Common errors**: triggers fire early → add flag checks.

## Recipe 04 — F10 “Start / Repeat / End” menu

- **Goal**: player-controlled training loop.
- **Ingredients**: 3 F10 items + flags.
- **Steps**:
  1. “Start” sets flag `10 = 1`, resets `20 = 0`
  2. “Repeat” resets target group (or re-activates a late-activated copy)
  3. “End” shows message and sets “mission complete” flag
- **Quick test**: you can restart the exercise without restarting the server.
- **Common errors**: menus not visible → wrong coalition.

## Recipe 05 — Objective counter (destroy 3 targets)

- **Goal**: simple win condition.
- **Ingredients**: 3 target groups + flags.
- **Steps**:
  1. Each target destroyed → increment a counter flag
  2. When counter reaches 3 → message “Success” + end logic
- **Quick test**: destroy targets, see counter progression.
- **Common errors**: wrong “group dead” condition → check group names.

