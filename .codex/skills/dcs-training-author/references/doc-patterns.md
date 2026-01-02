# DCS Docs / Lessons / Course Patterns

## Templates

### Language Bar (single line)

Use a single-line language bar at the top of each doc; bold the active language:

`🇬🇧 **English** | 🇪🇸 [Español](README.es.md) | 🇸🇪 [Svenska](README.sv.md) | 🇫🇮 [Suomi](README.fi.md)`

Rules:
- Use relative links.
- In each language file, keep links pointing to the matching language doc when it exists.

---

## Quick Takeoff Template (Markdown)

Title should be module-specific and short.

```
# <Module> — Quick Takeoff (DCS)

<Language bar>

Based on: <official manual link> (optional)

## Step-by-step (cheat sheet)

1. ...
2. ...

### Keyboard shortcuts / bindings

Bindings vary per user and module. Never claim module-specific defaults.

| Action | Keyboard/HOTAS | Notes |
| --- | --- | --- |
| Wheel brakes (hold) | `W` (common default; verify) | ... |
| Landing gear toggle | `G` (common default; verify) | ... |
| <Module control> | (bind) | ... |

### Mouse vs bindings

Say explicitly what can be done via cockpit mouse interaction and what you recommend binding.

## On the runway (before takeoff)

<numbered checklist + 1–2 why-notes>

## Takeoff (method 1: HUD)

<numbered steps>

## Takeoff (method 2: attitude indicator)

<numbered steps>

## Common mistakes

- ...

## Practice (5 minutes)

- ...
```

---

## Lesson Template (1 session)

Use when the user asks for a “tutorial”, “lesson”, “training”, or “teach me X”.

```
# <Module> — Lesson: <Topic>

<Language bar (optional)>

## Goal

In one sentence: what the learner can do at the end.

## Prerequisites

- DCS mode: `Game` / `Sim`
- Controls: keyboard/mouse or HOTAS
- Required mission setup (map, weather, time, loadout)

## Key concepts (short)

- 3–6 bullets

## Step-by-step

1. Do ...
2. Check ...
3. If wrong, recover by ...

## Bindings checklist

| Action | Keyboard/HOTAS | Notes |
| --- | --- | --- |
| ... | (bind) | ... |

## Common mistakes

- Symptom → likely cause → fix

## Debrief

- What “good” looks like
- What to practice next
```

---

## Course Template (multi-session)

Use when the user asks for a “course”, “curriculum”, “plan”, or “from zero to X”.

```
# <Module> — Course: <Title>

## Audience

Beginner / intermediate / returning pilot.

## Outcomes

By the end, the learner can:
1. ...
2. ...

## Structure

### Session 1 — <topic>
- Objectives
- Practice
- Homework

### Session 2 — <topic>
...

## Assessment (simple)

- Checkride / scenario mission / short quiz
```

---

## Translation / Localization Notes

- Prefer “same structure, localized words” over rewriting the teaching flow.
- Keep technical labels (`NAV`, `SPAK`, cockpit markings) as they appear in-cockpit; translate the explanation around them.
- If an action name differs across languages, keep the cockpit label and translate only the descriptive text.
- Do not invent keybind defaults; use “(bind)” placeholders.
