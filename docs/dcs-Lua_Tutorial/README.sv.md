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

- [Kapitel 01](ch01.sv.md) — Introduktion: DCS + Lua + vad scriptning möjliggör
- [Kapitel 02](ch02.sv.md) — Arbetsflöde/pipeline (VS Code), setup och vanliga bibliotek
- [Kapitel 03](ch03.sv.md) — Välkommen (Cap 0): första Lua‑vinsten
- [Kapitel 04](ch04.sv.md) — Var Lua körs i DCS
- [Kapitel 05](ch05.sv.md) — Variabler
- [Kapitel 06](ch06.sv.md) — Strings och `string.format`
- [Kapitel 07](ch07.sv.md) — Tabeller som CFG
- [Kapitel 08](ch08.sv.md) — If/Else + flags
- [Kapitel 09](ch09.sv.md) — Funktioner
- [Kapitel 10](ch10.sv.md) — Scheduler säkert
- [Kapitel 11](ch11.sv.md) — F10‑meny
- [Kapitel 12](ch12.sv.md) — Events + räknare
- [Kapitel 13](ch13.sv.md) — Struktur (`MyMission`)
- [Kapitel 14](ch14.sv.md) — Felsökning
- [Kapitel 15](ch15.sv.md) — Recept
