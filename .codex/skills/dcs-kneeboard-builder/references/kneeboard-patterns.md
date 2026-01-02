# DCS Kneeboard Patterns

Goal: cockpit-ready, scannable pages. Keep them short.

## General Rules

- One page = one job.
- Prefer “Do / Check / Notes”.
- Avoid paragraphs; prefer bullets, tables, and numbered steps.
- Keep cockpit labels literal (`NAV`, `SPAK`, etc.) and translate around them.
- If keybinds are mentioned, do not assume defaults; use “(bind)”.

## Checklist Page (Template)

```md
# <Aircraft> — <Checklist Name>

## Do

1. ...
2. ...

## Check

- ...

## Notes

- ...
```

## Radio Presets / Comms Page (Template)

```md
# <Aircraft> — Radios / Comms

| Use | Frequency | Mode | Notes |
| --- | --- | --- | --- |
| ATC | xxx.xxx | AM/FM | ... |
| Tower | xxx.xxx | AM | ... |
```

## Takeoff “Flow” Page (Template)

```md
# <Aircraft> — Takeoff Flow

1. Line up / brakes (bind or mouse)
2. Master mode / nav setup
3. Lights / warnings check
4. Power set
5. Rotate cues
6. Gear up / climb
```

## Emergency Page (Template)

```md
# <Aircraft> — Emergency: <Scenario>

## Immediate

1. ...

## If no improvement

1. ...

## Land ASAP

- ...
```

## Converting to Kneeboard Files (Notes)

DCS typically uses image-based kneeboard pages (PNG/JPG) placed under the user’s `Saved Games` kneeboard folder for the aircraft, but paths vary by install and module. When asked, provide:
- The markdown content (source of truth)
- A brief “export plan” (render markdown to PDF/PNG using the user’s preferred tooling)
