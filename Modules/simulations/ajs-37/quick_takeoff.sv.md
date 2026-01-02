# AJS-37 Viggen — Snabbguide: Start (DCS)

Språk:
🇬🇧 [English](quick_takeoff.en.md) · 🇪🇸 [Español](quick_takeoff.es.md) · 🇸🇪 [Svenska](quick_takeoff.sv.md) · 🇫🇮 [Suomi](quick_takeoff.fi.md)

Bygger på den officiella manualen: [docs/DCS_AJS37_Flight_Manual_EN.pdf](docs/DCS_AJS37_Flight_Manual_EN.pdf) (“Takeoff & Landing”).

## Steg-för-steg (fusklapp)

1. Rikta in på banan och håll hjulbroms.
2. `Master Mode`: `NAV` (ställ in minst 2 minuter innan startkraft).
3. (Vid behov) manuell initial kurs: rikta in på banriktningen → tryck `Reference`.
4. `SPAK`: `ON` (bekräfta lampan).
5. Landningsljus: `LANDNING` (ON).
6. Ge max effekt **utan efterbrännkammare** (håll EGT inom gränser).
7. Släpp broms och håll centerlinjen med pedaler.
8. Vid behov: tänd efterbrännkammare (kontrollera zon/tober/EPR).
9. Rotera med HUD:ens tid-/distansmarkeringar (eller Metod 2 hastigheter/attityder).
10. Positiv stigning: landställ upp (obs: klaffar dras in med landstället).
11. Fortsätt stiga tills FPV syns och HUD växlar till navigationssymbolik.
12. Höj HUD-glaset till inflight om du behöver symbolik vid lägre AoA.

### Tangentbord / bindningar

I DCS kan bindningar skilja sig och många modulspecifika reglage kan vara obundna som standard. Använd detta som en checklista för vad som bör bindas (plus ett par vanliga DCS-standarder):

| Funktion | Tangent | Not |
| --- | --- | --- |
| Hjulbroms (håll) | `W` (vanlig standard) | Håll när du ger effekt. |
| Landställ (toggle) | `G` (vanlig standard) | Landställ upp när du är i luften. |
| `Master Mode` → `NAV` | (binda) | Viktigt: 2 min innan startkraft. |
| `SPAK` ON/OFF | (binda) | Bekräfta ON före start. |
| `Reference` (spak) | (binda) | För manuell initial kurs. |
| HUD-glas upp/ner | (binda) | Bra för manuell kurs / symbolik vid låg AoA. |

## Innan du kör ut på banan (snabbt)

- Flygplanet klart (motor igång, generator ON, grundsystem stabila).
- Ställ in det viktigaste för start + navigering: `Master Mode` och HUD.

## På banan (Before take-off)

![Before take-off checklist](assets/quick_takeoff_assets/before_takeoff.png)

1. Rikta in flygplanet mot banan.
2. Kontrollera: huvudkurs, reservkurs, reservhorisont och höjdmätare.
3. `Master Mode selector`: `NAV` (minst 2 minuter innan startkraft, för att undvika navigationsproblem).
4. Manuell kursinställning (vid behov): när du står noggrant i banriktningen, tryck `Reference` (på spaken).
5. `SPAK`: `ON`, kontrollera att lampan lyser.
6. Master Caution / varningslampor: kontroll (lampan `X-TANK BRÄ` brukar slockna först efter ~70% RPM).
7. HUD-symbolik: kontrollera att den ser rimlig ut.
8. Landningsljus: `LANDNING` (ON).

Manualnotis: Radar och Centralindikatorn (CI) fungerar först ~30 s efter att `Master Mode` satts till `NAV`, och ~180 s efter att generatorn är på (mjukvaruinitiering).

### Manuell initial kurs (endast vid behov)

Bra om banan är hal och du har kraftig sidvind.

1. `Master Mode selector`: `NAV`.
2. Höj HUD-glaset till “inflight” (övre läget).
3. Rikta in noggrant mot banriktningen.
4. Tryck `Reference` (på spaken).
5. Sänk HUD-glaset till “takeoff/landing” (nedre läget).

För att nollställa en manuell initial kurs: växla `Master Mode` `NAV → BER → NAV` (gäller även om du vill tillbaka till automatisk initial kurs).

## Metod 1: start med HUD (rekommenderad)

![Takeoff using the HUD](assets/quick_takeoff_assets/takeoff_hud_method.png)

1. Håll hjulbroms.
2. Ge max effekt **utan efterbrännkammare**.
   - Kontrollera EGT (max `590°C + utomhustemperatur`).
3. Släpp broms, styr med pedaler.
4. Vid behov: tänd efterbrännkammare.
   - Kontrollera:
     - Zonindikator = önskad zon.
     - Utblås/toberindikator = önskad zon uppnådd.
     - EPR (tryckförhållande):
       - Zon 2: `< +15°C` → `> 1.9`
       - Zon 2: `> +15°C` → `> 1.8`
       - Zon 3: max effekt.
5. Kontrollera IAS och tid-/distanslinjen.
6. Rotera när tid-/distanslinjen når markeringarna.
   - Sätt flygbanevektorn (FPV) till:
     - Utan EBK: på horisontlinjen.
     - Med EBK: ungefär vid de yttre stolparnas höjd (≈ `3°` över horisonten).
7. Bekräfta att farten fortsätter öka.
8. Landställ upp när du är i luften.
   - Not: när landstället går upp dras klaffarna in; räkna med liten minskning i lyft.
9. Stig med vald attityd tills FPV syns; HUD ska normalt växla från startsymbolik till navigationsläge.
10. Höj HUD-glaset till inflight-läge om du behöver symbolik vid lägre anfallsvinkel.

## Metod 2: start med attitydindikatorn

![Takeoff using attitude indicator](assets/quick_takeoff_assets/takeoff_attitude_method.png)

1. Steg 1–4: samma som HUD-metoden.
2. Rotera:
   - Vid `280 km/h`: till `10°` stigning (max effekt utan EBK).
   - Vid `250 km/h`: till `13°` stigning (med EBK).
3. Landställ upp när du är i luften (samma not om klaffar/lyft).
4. Höj HUD-glaset till inflight om du behöver HUD-symbolik vid låg AoA.

## Snabba säkerhetsnotiser

- Hal bana + kraftig sidvind: använd manuell initial kurs.
- Känner du ett “lyftdip” när landstället går upp: stabilisera attityd och fart, överkorrigera inte.
