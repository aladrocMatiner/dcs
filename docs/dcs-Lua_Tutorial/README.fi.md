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

- Luku 01 — Johdanto: DCS + Lua + mitä skriptaus mahdollistaa: [ch01.fi.md](ch01.fi.md)
- Luku 02 — Työputki (VS Code), asennukset ja yleiset kirjastot: [ch02.fi.md](ch02.fi.md)
- Luku 03 — Tervetuloa (Cap 0): ensimmäinen onnistuminen: [ch03.fi.md](ch03.fi.md)
- Luku 04 — Missä Lua ajetaan DCS:ssä: [ch04.fi.md](ch04.fi.md)
- Luku 05 — Muuttujat: [ch05.fi.md](ch05.fi.md)
- Luku 06 — Merkkijonot ja `string.format`: [ch06.fi.md](ch06.fi.md)
- Luku 07 — CFG‑taulukko: [ch07.fi.md](ch07.fi.md)
- Luku 08 — If/Else + flagit: [ch08.fi.md](ch08.fi.md)
- Luku 09 — Funktiot: [ch09.fi.md](ch09.fi.md)
- Luku 10 — Turvallinen ajastus: [ch10.fi.md](ch10.fi.md)
- Luku 11 — F10‑valikko: [ch11.fi.md](ch11.fi.md)
- Luku 12 — Tapahtumat + laskuri: [ch12.fi.md](ch12.fi.md)
- Luku 13 — Rakenne (`MyMission`): [ch13.fi.md](ch13.fi.md)
- Luku 14 — Vianhaku: [ch14.fi.md](ch14.fi.md)
- Luku 15 — Reseptit: [ch15.fi.md](ch15.fi.md)
