# Cookbook — Recept för Mission Editor (utan Lua)

🇬🇧 [English](cookbook.md) | 🇪🇸 [Español](cookbook.es.md) | 🇸🇪 **Svenska** | 🇫🇮 [Suomi](cookbook.fi.md)

Till index: [README.sv.md](README.sv.md)

Varje recept: **Mål → Ingredienser → Steg → Quick test → Vanliga fel**.

## Recept 01 — Meddelande när spelaren går in i zon

- **Mål**: visa “du är i träningsområdet”.
- **Ingredienser**: en zon + en trigger.
- **Steg**:
  1. Skapa `ZONE_TRAINING`
  2. Trigger: villkor “spelare i zon”
  3. Åtgärd: meddelande
- **Quick test**: flyg in i zonen, se meddelandet en gång.
- **Vanliga fel**: spam → flag‑gate.

## Recept 02 — Late‑activated konvoj på kommando

- **Mål**: minska last tills det behövs.
- **Ingredienser**: `RED_CONVOY_01` med Late Activation.
- **Steg**:
  1. Slå på Late Activation
  2. Villkor: tid > 60s (eller spelare i zon)
  3. Åtgärd: Activate group `RED_CONVOY_01`
- **Quick test**: konvojen dyker upp först när triggern går.
- **Vanliga fel**: fel gruppnamn.

## Recept 03 — Tre faser med flags

- **Mål**: ren mission‑logik.
- **Ingredienser**: flags `10` (start), `20` (klart).
- **Steg**:
  1. F10 “Start exercise” → `10 = 1`
  2. Zontrigger bara om `10 == 1`
  3. Vid klart: `20 = 1` + “RTB”
- **Quick test**: faser sker i ordning.
- **Vanliga fel**: triggar tidigt → fler flag‑checks.

## Recept 04 — F10 “Start / Repeat / End”

- **Mål**: spelarkontrollerad träningsloop.
- **Ingredienser**: 3 F10‑items + flags.
- **Steg**:
  1. “Start” sätter `10 = 1`, reset `20 = 0`
  2. “Repeat” reset/aktivera mål igen
  3. “End” meddelande + slutflag
- **Quick test**: repetera utan serverrestart.
- **Vanliga fel**: meny syns inte → fel koalition.

## Recept 05 — Målräknare (förstör 3)

- **Mål**: enkel vinstvillkor.
- **Ingredienser**: 3 målgrupper + flag‑räknare.
- **Steg**:
  1. Varje mål förstört → öka räknarflag
  2. När 3 → “Success” + slutlogik
- **Quick test**: progression när mål förstörs.
- **Vanliga fel**: fel “group dead” → kontrollera grupp.

