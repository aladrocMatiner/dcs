# Cookbook — Mission Editor ‑reseptit (ilman Luaa)

🇬🇧 [English](cookbook.md) | 🇪🇸 [Español](cookbook.es.md) | 🇸🇪 [Svenska](cookbook.sv.md) | 🇫🇮 **Suomi**

Takaisin indeksiin: [README.fi.md](README.fi.md)

Jokainen resepti: **Tavoite → Tarvikkeet → Vaiheet → Quick test → Yleiset virheet**.

## Resepti 01 — Viesti kun pelaaja menee zoneen

- **Tavoite**: kertoa “olet harjoitusalueella”.
- **Tarvikkeet**: zone + yksi trigger.
- **Vaiheet**:
  1. Luo `ZONE_TRAINING`
  2. Trigger: ehto “pelaaja zonessa”
  3. Toiminto: viesti
- **Quick test**: lennä zoneen, viesti kerran.
- **Yleiset virheet**: spämmi → flag‑portti.

## Resepti 02 — Late‑activated saattue käynnistyy pyynnöstä

- **Tavoite**: vähennä kuormaa kunnes tarvitaan.
- **Tarvikkeet**: `RED_CONVOY_01` Late Activation ‑tilassa.
- **Vaiheet**:
  1. Ota Late Activation käyttöön
  2. Ehto: aika > 60s (tai pelaaja zonessa)
  3. Toiminto: Activate group `RED_CONVOY_01`
- **Quick test**: saattue ilmestyy vasta triggerin jälkeen.
- **Yleiset virheet**: väärä nimi.

## Resepti 03 — Kolme vaihetta flageilla

- **Tavoite**: siisti mission kulku.
- **Tarvikkeet**: flagit `10` (start), `20` (valmis).
- **Vaiheet**:
  1. F10 “Start exercise” → `10 = 1`
  2. Zone‑trigger vain jos `10 == 1`
  3. Kun valmis: `20 = 1` + “RTB”
- **Quick test**: vaiheet järjestyksessä.
- **Yleiset virheet**: triggerit liian aikaisin → lisää flag‑checkit.

## Resepti 04 — F10 “Start / Repeat / End”

- **Tavoite**: pelaajan ohjaama harjoituslooppi.
- **Tarvikkeet**: 3 F10‑itemiä + flagit.
- **Vaiheet**:
  1. “Start” asettaa `10 = 1`, reset `20 = 0`
  2. “Repeat” resetoi/aktivoi kohteet uudelleen
  3. “End” viesti + loppuflagi
- **Quick test**: voit toistaa ilman serverin restarttia.
- **Yleiset virheet**: valikko ei näy → väärä koalitio.

## Resepti 05 — Kohdelaskuri (tuhoa 3)

- **Tavoite**: yksinkertainen voittoehto.
- **Tarvikkeet**: 3 kohderyhmää + laskuriflagi.
- **Vaiheet**:
  1. Jokainen kohde tuhottu → kasvata laskuria
  2. Kun 3 → “Success” + lopetus
- **Quick test**: eteneminen näkyy tuhoutuessa.
- **Yleiset virheet**: väärä “group dead” ‑ehto.

