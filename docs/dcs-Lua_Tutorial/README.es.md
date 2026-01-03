# Tutorial de Lua para DCS

🇬🇧 [English](README.md) | 🇪🇸 **Español** | 🇸🇪 [Svenska](README.sv.md) | 🇫🇮 [Suomi](README.fi.md)

Este tutorial se centra en **scripting de misiones con Lua en DCS**, no en la aviónica del avión ni en el modding. La idea es ser práctico, apto para principiantes y avanzar capítulo a capítulo.

## Cómo usar este tutorial (sin frustración)

- Lee un capítulo y haz su “Prueba rápida” antes de seguir.
- Cambia **una sola cosa** cada vez.
- Si algo falla, vuelve a la versión más simple (un solo `outText`) y avanza de nuevo.
- Guarda la misión cada vez que cambias el script o el trigger.

## Cómo ejecutar los ejemplos en DCS (Mission Editor)

Tienes dos maneras. Usa la que sea más cómoda para ti:

### Opción A — `DO SCRIPT` (pegar texto)

1) Mission Editor → *Triggers*
2) Trigger: `MISSION START`
3) Action: `DO SCRIPT`
4) Pega el bloque `lua` del capítulo.

Es rápido, pero para proyectos reales es mejor la Opción B.

### Opción B — `DO SCRIPT FILE` (archivo `.lua`)

1) Abre el capítulo y mira el archivo del ejemplo (carpeta [examples/](examples/)).
2) Mission Editor → *Triggers*
3) Trigger: `MISSION START`
4) Action: `DO SCRIPT FILE`
5) Selecciona el `.lua` (por ejemplo `examples/ex03_hello.lua`).
6) Guarda la misión (normalmente DCS guarda el script dentro de la `.miz`).
7) Ejecuta la misión.

### Cómo “ver” resultados (muy importante)

- En pantalla: `trigger.action.outText("texto", 10)` (lo verás siempre).
- En logs: `env.info("mensaje")` (búscalo en `Saved Games\\DCS\\Logs\\dcs.log`).

> **Si te sale error, haz esto:**
> - Vuelve al Capítulo 03 y asegúrate de que tu “mensaje de vida” aparece en pantalla.
> - Si no aparece, el problema no es Lua: es el trigger/archivo/guardado.

## Seguridad y límites (sin miedo, pero con cabeza)

En muchas instalaciones, el entorno de misión (MSE) está **sanitizado** por seguridad. Algunas librerías de Lua (`io`, `os`, `lfs`) pueden estar deshabilitadas o restringidas. En este tutorial no te damos instrucciones para cambiar eso; trabajamos con scripts que funcionan dentro de los límites normales de una misión.

## Capítulos

- Capítulo 01 — Introducción: DCS + Lua + para qué sirve el scripting: [ch01.es.md](ch01.es.md)
- Capítulo 02 — Pipeline de trabajo (VS Code), configuración y librerías comunes: [ch02.es.md](ch02.es.md)
- Capítulo 03 — Bienvenida (Cap 0): tu primer éxito con Lua en DCS: [ch03.es.md](ch03.es.md)
- Capítulo 04 — Dónde vive Lua en DCS (y dónde pegarlo): [ch04.es.md](ch04.es.md)
- Capítulo 05 — Variables (sin miedo): guardar datos: [ch05.es.md](ch05.es.md)
- Capítulo 06 — Strings y mensajes bonitos (`string.format`): [ch06.es.md](ch06.es.md)
- Capítulo 07 — Tablas como configuración (CFG): [ch07.es.md](ch07.es.md)
- Capítulo 08 — If/Else + Flags: decisiones simples: [ch08.es.md](ch08.es.md)
- Capítulo 09 — Funciones: deja de copiar/pegar: [ch09.es.md](ch09.es.md)
- Capítulo 10 — Tiempo y scheduler seguro: [ch10.es.md](ch10.es.md)
- Capítulo 11 — Menú F10: controles para el jugador: [ch11.es.md](ch11.es.md)
- Capítulo 12 — Eventos: contador / scoreboard simple: [ch12.es.md](ch12.es.md)
- Capítulo 13 — Orden y estructura: `MyMission` + config + lógica: [ch13.es.md](ch13.es.md)
- Capítulo 14 — Depuración sin drama: checklist: [ch14.es.md](ch14.es.md)
- Capítulo 15 — Biblioteca de recetas copiables: [ch15.es.md](ch15.es.md)
