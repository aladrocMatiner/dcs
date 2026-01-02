# AJS-37 Viggen (DCS) — Aloittelijan Opas (Pedagoginen)

Tämä on käytännöllinen, vaiheittainen opas sinulle, joka olet uusi lentosimulaattoreissa ja uusi Viggenissä.
Tavoite: pääset nopeasti tilanteesta “en tiedä mitä tehdä” tilanteeseen “osaan käynnistää, rullata, nousta, navigoida yksinkertaisesti ja laskeutua”.

Kielivalinta / Languages:
🇬🇧 `beginner_manual.en.md` · 🇪🇸 `beginner_manual.es.md` · 🇸🇪 `beginner_manual.sv.md` · 🇫🇮 `beginner_manual.fi.md`

Virallinen viite: `../DCS_AJS37_Flight_Manual_EN.pdf` (moduulin käsikirja).

## 0) Mitä Opit

Opit tässä järjestyksessä:

1. Tunnistamaan ohjaamon alueet ja tärkeimmät mittarit.
2. Käynnistämään koneen, rullaamaan ja nousemaan turvallisesti.
3. Lentämään yksinkertaisen navigoinnin (tila `NAV`).
4. Laskeutumaan vakaasti ja hallitusti.

Jos haluat vain ilmaan nopeasti, käytä `quick_takeoff.md`.

## 1) Ohjaamo Karttana (Älä Yritä Muistaa Kaikkea)

Opettele ensin *missä* asiat ovat:

![Ohjaamon yleisasettelu](pedagogical_assets/cockpit_layout.png)

- **Etupaneeli**: tärkeimmät lentomittarit + HUD + varoitusvalot.
- **Vasen sivu**: paljon järjestelmäkytkimiä (moottori, sähkö jne.).
- **Oikea sivu**: lisää järjestelmiä ja indikaattoreita.

Etupaneelin yleiskuva:

![Etupaneeli](pedagogical_assets/front_panel.png)

### 6 Asiaa, Joita Seuraat Aina

1. **Nopeus** (km/h): riittääkö nousuun / nousukiitoon / laskuun?
2. **Korkeus** (m): nousetko/laskeudutko odotetusti?
3. **Asento** (pitch/roll): pysyykö kone vakaana? vedätkö liikaa?
4. **Moottori**: RPM / EGT / EPR (työntövoima ja lämpötilat).
5. **Varoitukset**: master caution ja varoitusvalot.
6. **HUD** (jos käytössä): noususymboliikka ja lentorata-/FPV‑viitteet.

## 2) Ennen Aloitusta (Ohjaimet)

- Määritä: pitch/roll/yaw, pyöräjarru, kaasu (throttle), laskuteline, trimmi.
- Jos sinulla ei ole polkimia: varmista, että peräsinakseli (twist) on pehmeä.
- Löydä ja opettele käyttämään:
  - `Master Mode` (normaali lentäminen: `NAV`)
  - `SPAK` (vakautus/autopilotti) — valinnainen mutta hyödyllinen

## 3) Rullaus (Taxi) — Yleinen Aloittelijan Kompastus

Moni rikkoo koneen jo maassa.

- Tyhjäkäynnilläkin on paljon työntövoimaa: tee pieniä kaasumuutoksia.
- Ohjaus polkimilla; tiukempiin käännöksiin voi tarvita differentiaalijarrutusta.
- Jos käytät työntövoiman kääntöä maassa: varmista, että takana on tilaa.

Tavoite: pääset kiitotielle rauhallisesti ja hallitusti.

## 4) Nousu (Aloittelijalle Suositeltu)

Käytä HUD‑menetelmää virallisesta proseduurista.

Ennen kiihdytystä:

- Asetu kiitotien suuntaan.
- Aseta `Master Mode` → `NAV` **vähintään 2 minuuttia** ennen nousutehoa.
- Laskuvalo `LANDNING` ON.

Yksinkertaistettu:

1. Pidä pyöräjarru.
2. Täysi teho **ilman jälkipolttoa**.
3. Vapauta jarru ja pidä keskilinja polkimilla.
4. Tarvittaessa (lyhyt kiitotie/raskas kuorma): sytytä jälkipoltto.
5. Nosta nokka (rotate) HUD‑merkintöjen mukaan.
6. Ilmassa: laskuteline ylös.

Viite: `quick_takeoff.md` sisältää täydellisen checklistin ja kuvat.

## 5) Ensimmäinen Navigointi (Pidä Se Yksinkertaisena)

Viggen on tehty suunniteltuun navigointiin. Aloittelijana:

- Lennä `NAV`‑tilassa.
- Nousun jälkeen: pidä kiitotien suunta, nouse vakaasti, käänny vasta sitten selkeään maamerkkiin.
- Älä “metsästä nappeja” heti nousun jälkeen: lennä ensin.

Hyvä suoritus näyttää tältä:

- Vakaat nousut.
- Vakaat nopeudet.
- Ei varoituksia.
- Pehmeät käännökset.

## 6) Lasku (Lempeä Kierros)

Lennä leveä, rauhallinen laskukierros. Älä syöksy kiitotielle.

Tavoitteet:

- Tule finaaliin linjassa ja vakaana.
- Ota laskuteline ulos ajoissa.
- Pidä turvallinen AoA/nopeus.

Vinkki: harjoittele touch‑and‑go’ta tyynessä säässä.

## 7) Tyypilliset Virheet (Ja Korjaukset)

- **Liian raju rotate** → Nosta nokkaa pehmeästi; käytä asennon viitteitä.
- **HUDin “jahtaaminen”** → Lennä asento + nopeus; HUD on vahvistus, ei ohjaaja.
- **Liian kova rullaus** → Tyhjäkäynti työntää; jarruta ajoissa.
- **`NAV`-ajastuksen unohtaminen** → Aseta `NAV` vähintään 2 min ennen nousutehoa.

## 8) Seuraava Askel (Valitse Yksi)

- Harjoitus: 10 nousua + 10 laskua (sama kenttä, ei aseita).
- Lisää 1 taito: perus reittinavigointi tai yksinkertainen aseiden käyttö.

