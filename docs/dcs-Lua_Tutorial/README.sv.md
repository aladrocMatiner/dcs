# Lua‑tutorial för DCS

🇬🇧 [English](README.md) | 🇪🇸 [Español](README.es.md) | 🇸🇪 **Svenska** | 🇫🇮 [Suomi](README.fi.md)

Den här guiden handlar om **Lua‑scriptning för DCS‑uppdrag**, inte flygplanens avionik eller modding. Målet är att vara praktisk, nybörjarvänlig och byggas upp kapitel för kapitel.

## Så använder du guiden (låg frustration)

- Läs ett kapitel och gör “Snabbtest” innan du går vidare.
- Ändra **en sak i taget**.
- Om något går fel: gå tillbaka till enklaste versionen (en `outText`) och bygg upp igen.
- Spara uppdraget varje gång du ändrar triggers eller skript.

## Så kör du exemplen i DCS (Mission Editor)

### Alternativ A — `DO SCRIPT` (klistra in)

1) Mission Editor → *Triggers*
2) `MISSION START`
3) `DO SCRIPT`
4) Klistra in kapitelns `lua`‑block.

### Alternativ B — `DO SCRIPT FILE` (rekommenderas)

1) Öppna kapitlet och hitta filen i [examples/](examples/).
2) Mission Editor → *Triggers* → `MISSION START`
3) `DO SCRIPT FILE` → välj `.lua`‑filen (t.ex. `examples/ex03_hello.lua`)
4) Spara uppdraget och kör.

### Så ser du resultat

- Skärm: `trigger.action.outText("text", 10)`
- Logg: `env.info("message")` → `Saved Games\\DCS\\Logs\\dcs.log`

## Säkerhet / begränsningar

MSE är ofta **sanitiserat**. Vissa Lua‑libbar (`io`, `os`, `lfs`) kan vara avstängda eller begränsade. Den här guiden ger inga instruktioner för att ändra det.

## Kapitel

- Kapitel 01 — Introduktion: DCS + Lua + vad scriptning möjliggör: [ch01.sv.md](ch01.sv.md)
- Kapitel 02 — Arbetsflöde/pipeline (VS Code), setup och vanliga bibliotek: [ch02.sv.md](ch02.sv.md)
- Kapitel 03 — Välkommen (Cap 0): första Lua‑vinsten: [ch03.sv.md](ch03.sv.md)
- Kapitel 04 — Var Lua körs i DCS: [ch04.sv.md](ch04.sv.md)
- Kapitel 05 — Variabler: [ch05.sv.md](ch05.sv.md)
- Kapitel 06 — Strings och `string.format`: [ch06.sv.md](ch06.sv.md)
- Kapitel 07 — Tabeller som CFG: [ch07.sv.md](ch07.sv.md)
- Kapitel 08 — If/Else + flags: [ch08.sv.md](ch08.sv.md)
- Kapitel 09 — Funktioner: [ch09.sv.md](ch09.sv.md)
- Kapitel 10 — Scheduler säkert: [ch10.sv.md](ch10.sv.md)
- Kapitel 11 — F10‑meny: [ch11.sv.md](ch11.sv.md)
- Kapitel 12 — Events + räknare: [ch12.sv.md](ch12.sv.md)
- Kapitel 13 — Struktur (`MyMission`): [ch13.sv.md](ch13.sv.md)
- Kapitel 14 — Felsökning: [ch14.sv.md](ch14.sv.md)
- Kapitel 15 — Recept: [ch15.sv.md](ch15.sv.md)
