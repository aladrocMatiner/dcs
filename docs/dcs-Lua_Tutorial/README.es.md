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

- [Capítulo 01](ch01.es.md) — Introducción: DCS + Lua + para qué sirve el scripting
- [Capítulo 02](ch02.es.md) — Pipeline de trabajo (VS Code), configuración y librerías comunes
- [Capítulo 03](ch03.es.md) — Bienvenida (Cap 0): tu primer éxito con Lua en DCS
- [Capítulo 04](ch04.es.md) — Dónde vive Lua en DCS (y dónde pegarlo)
- [Capítulo 05](ch05.es.md) — Variables (sin miedo): guardar datos
- [Capítulo 06](ch06.es.md) — Strings y mensajes bonitos (`string.format`)
- [Capítulo 07](ch07.es.md) — Tablas como configuración (CFG)
- [Capítulo 08](ch08.es.md) — If/Else + Flags: decisiones simples
- [Capítulo 09](ch09.es.md) — Funciones: deja de copiar/pegar
- [Capítulo 10](ch10.es.md) — Tiempo y scheduler seguro
- [Capítulo 11](ch11.es.md) — Menú F10: controles para el jugador
- [Capítulo 12](ch12.es.md) — Eventos: contador / scoreboard simple
- [Capítulo 13](ch13.es.md) — Orden y estructura: `MyMission` + config + lógica
- [Capítulo 14](ch14.es.md) — Depuración sin drama: checklist
- [Capítulo 15](ch15.es.md) — Biblioteca de recetas copiables
