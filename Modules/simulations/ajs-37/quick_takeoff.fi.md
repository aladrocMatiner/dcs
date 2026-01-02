# AJS-37 Viggen — Pikaopas: Nousu (DCS)

Kieli:
🇬🇧 [English](quick_takeoff.en.md) · 🇪🇸 [Español](quick_takeoff.es.md) · 🇸🇪 [Svenska](quick_takeoff.sv.md) · 🇫🇮 [Suomi](quick_takeoff.fi.md)

Perustuu viralliseen käsikirjaan: [docs/DCS_AJS37_Flight_Manual_EN.pdf](docs/DCS_AJS37_Flight_Manual_EN.pdf) (“Takeoff & Landing”).

## Ennen kiitotielle siirtymistä (nopeasti)

- Kone valmis (moottori käynnissä, generaattori ON, perusjärjestelmät vakaat).
- Aseta minimi nousuun + navigointiin: `Master Mode` ja HUD.

## Kiitotiellä (Before take-off)

![Before take-off checklist](assets/quick_takeoff_assets/before_takeoff.png)

1. Asetu kiitotien suuntaan.
2. Tarkista: pääkurssi, varakurssi, varahorisontti ja korkeusmittari.
3. `Master Mode selector`: `NAV` (vähintään 2 minuuttia ennen nousutehoa, jotta navigointi ei sekoa).
4. Manuaalinen kurssiasetus (tarvittaessa): kun olet tarkasti kiitotien suunnassa, paina `Reference` (sauvassa).
5. `SPAK`: `ON`, varmista että merkkivalo palaa.
6. Master Caution / varoitusvalot: tarkista (valo `X-TANK BRÄ` sammuu usein ensimmäisenä ~70% RPM jälkeen).
7. HUD-symbologia: varmista että se näyttää järkevältä.
8. Laskuvalo: `LANDNING` (ON).

Muistio käsikirjasta: tutka ja keski-indikaattori (CI) toimivat vasta ~30 s sen jälkeen kun `Master Mode` on `NAV`, ja ~180 s generaattorin kytkemisen jälkeen (ohjelmiston alustus).

### Manuaalinen alkuperäiskurssi (vain jos tarvitset)

Hyödyllinen liukkaalla kiitotiellä ja kovassa sivutuulessa.

1. `Master Mode selector`: `NAV`.
2. Nosta HUD-lasi “inflight”-asentoon (yläasento).
3. Asetu tarkasti kiitotien suuntaan.
4. Paina `Reference` (sauvassa).
5. Laske HUD-lasi “takeoff/landing”-asentoon (ala-asento).

Manuaalisen asetuksen nollaus: vaihda `Master Mode` `NAV → BER → NAV` (sama myös jos haluat takaisin automaattiseen alkuasetukseen).

## Menetelmä 1: nousu HUD:lla (suositeltu)

![Takeoff using the HUD](assets/quick_takeoff_assets/takeoff_hud_method.png)

1. Pidä pyöräjarru.
2. Täysi teho **ilman jälkipolttoa**.
   - Tarkista EGT (max `590°C + ulkolämpötila`).
3. Vapauta jarru ja pidä suunta polkimilla.
4. Tarvittaessa: sytytä jälkipoltto.
   - Tarkista:
     - Zonen merkkivalo = haluttu vyöhyke.
     - Suutin-/toberindikaattori = vyöhyke saavutettu.
     - EPR (paine­suhde):
       - Vyöhyke 2: `< +15°C` → `> 1.9`
       - Vyöhyke 2: `> +15°C` → `> 1.8`
       - Vyöhyke 3: maksimi teho.
5. Tarkista IAS ja aika-/matkaviiva.
6. Nosta nokka (rotate) kun aika-/matkaviiva saavuttaa merkit.
   - Aseta lentoratavektori (FPV):
     - Ilman jälkipolttoa: horisonttiviivalle.
     - Jälkipoltolla: noin ulompien pylväiden korkeudelle (≈ `3°` horisontin yläpuolelle).
7. Varmista, että nopeus kasvaa edelleen.
8. Teline ylös, kun olet ilmassa.
   - Huom: telineen sisäänvedon yhteydessä laipat vetäytyvät; odota pientä nostovoiman vähenemistä.
9. Nouse valitulla asennolla kunnes FPV ilmestyy; HUD yleensä vaihtaa automaattisesti noususymbologiasta normaaliin navigointiin.
10. Nosta HUD-lasi inflight-asentoon, jos tarvitset symbologiaa pienemmillä AoA-arvoilla.

## Menetelmä 2: nousu asentoindikaattorilla

![Takeoff using attitude indicator](assets/quick_takeoff_assets/takeoff_attitude_method.png)

1. Vaiheet 1–4: kuten HUD-menetelmä.
2. Rotate:
   - `280 km/h`: `10°` nousuasentoon (maksimi ilman jälkipolttoa).
   - `250 km/h`: `13°` nousuasentoon (jälkipoltolla).
3. Teline ylös ilmassa (sama huomio laipoista/nostosta).
4. Nosta HUD-lasi inflight-asentoon, jos tarvitset HUD-symbologiaa matalalla AoA:lla.

## Nopeat turvallisuusmuistiinpanot

- Liukas kiitotie + kova sivutuuli: käytä manuaalista alkuperäiskurssia.
- Jos tunnet pienen “dippauksen” nostossa telineen noustessa: älä taistele sitä vastaan—vakauta asento ja nopeus.
