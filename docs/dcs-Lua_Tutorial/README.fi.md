# Lua‑opas DCS:lle

🇬🇧 [English](README.md) | 🇪🇸 [Español](README.es.md) | 🇸🇪 [Svenska](README.sv.md) | 🇫🇮 **Suomi**

Tämä opas käsittelee **DCS‑tehtävien (mission) Lua‑skriptausta**, ei koneiden avionikkaa tai modausta. Tavoite on olla käytännöllinen, aloittelijaystävällinen ja edetä luku kerrallaan.

## Miten tätä opasta käytetään (ilman turhautumista)

- Lue yksi luku ja tee sen “Pikatesti” ennen seuraavaa.
- Muuta **vain yhtä asiaa kerrallaan**.
- Jos jokin menee rikki, palaa helpoimpaan versioon (yksi `outText`) ja rakenna uudelleen.
- Tallenna tehtävä aina kun muutat triggereitä tai skriptejä.

## Miten esimerkit ajetaan DCS:ssä (Mission Editor)

### Vaihtoehto A — `DO SCRIPT` (liitä)

1) Mission Editor → *Triggers*
2) `MISSION START`
3) `DO SCRIPT`
4) Liitä luvun `lua`‑blokki.

### Vaihtoehto B — `DO SCRIPT FILE` (suositus)

1) Avaa luku ja etsi tiedosto kansiosta [examples/](examples/).
2) Mission Editor → *Triggers* → `MISSION START`
3) `DO SCRIPT FILE` → valitse `.lua` (esim. `examples/ex03_hello.lua`)
4) Tallenna ja aja tehtävä.

### Miten näet tulokset

- Ruudulla: `trigger.action.outText("text", 10)`
- Lokissa: `env.info("message")` → `Saved Games\\DCS\\Logs\\dcs.log`

## Turvallisuus / rajoitukset

MSE on usein **sanitisoitu**. Osa Lua‑kirjastoista (`io`, `os`, `lfs`) voi olla pois käytöstä tai rajoitettu. Tässä oppaassa ei anneta ohjeita sen muuttamiseen.

## Luvut

- [Luku 01](ch01.fi.md) — Johdanto: DCS + Lua + mitä skriptaus mahdollistaa
- [Luku 02](ch02.fi.md) — Työputki (VS Code), asennukset ja yleiset kirjastot
- [Luku 03](ch03.fi.md) — Tervetuloa (Cap 0): ensimmäinen onnistuminen
- [Luku 04](ch04.fi.md) — Missä Lua ajetaan DCS:ssä
- [Luku 05](ch05.fi.md) — Muuttujat
- [Luku 06](ch06.fi.md) — Merkkijonot ja `string.format`
- [Luku 07](ch07.fi.md) — CFG‑taulukko
- [Luku 08](ch08.fi.md) — If/Else + flagit
- [Luku 09](ch09.fi.md) — Funktiot
- [Luku 10](ch10.fi.md) — Turvallinen ajastus
- [Luku 11](ch11.fi.md) — F10‑valikko
- [Luku 12](ch12.fi.md) — Tapahtumat + laskuri
- [Luku 13](ch13.fi.md) — Rakenne (`MyMission`)
- [Luku 14](ch14.fi.md) — Vianhaku
- [Luku 15](ch15.fi.md) — Reseptit
