# Cookbook — Recetas del Editor de Misiones (sin Lua)

🇬🇧 [English](cookbook.md) | 🇪🇸 **Español** | 🇸🇪 [Svenska](cookbook.sv.md) | 🇫🇮 [Suomi](cookbook.fi.md)

Volver al índice: [README.es.md](README.es.md)

Cada receta: **Objetivo → Ingredientes → Pasos → Quick test → Errores típicos**.

## Receta 01 — Mensaje al entrar en una zona

- **Objetivo**: enseñar “estás en la zona de entrenamiento”.
- **Ingredientes**: una zona + un trigger.
- **Pasos**:
  1. Crea `ZONE_TRAINING`
  2. Trigger: condición “jugador en zona”
  3. Acción: mensaje “Has entrado en la zona”
- **Quick test**: entra en zona, mensaje una vez.
- **Errores típicos**: spam → gate con flag.

## Receta 02 — Convoy late-activated bajo demanda

- **Objetivo**: reducir carga hasta que haga falta.
- **Ingredientes**: `RED_CONVOY_01` con Late Activation.
- **Pasos**:
  1. Marca Late Activation
  2. Condición: tiempo > 60s (o jugador en zona)
  3. Acción: Activate group `RED_CONVOY_01`
- **Quick test**: el convoy aparece solo cuando toca.
- **Errores típicos**: nombre mal → revisa el nombre del grupo.

## Receta 03 — Misión en 3 fases con flags

- **Objetivo**: flujo limpio sin triggers spaghetti.
- **Ingredientes**: flags `10` (started), `20` (complete).
- **Pasos**:
  1. F10 “Start exercise” → flag `10 = 1`
  2. Trigger de zona solo si `10 == 1`
  3. Al completar: flag `20 = 1` + mensaje “RTB”
- **Quick test**: fases en orden y sin activarse antes.
- **Errores típicos**: se dispara antes → añade checks de flags.

## Receta 04 — F10 “Start / Repeat / End”

- **Objetivo**: loop de entrenamiento controlado por el jugador.
- **Ingredientes**: 3 items F10 + flags.
- **Pasos**:
  1. “Start” pone `10 = 1` y resetea `20 = 0`
  2. “Repeat” resetea/reativa objetivos
  3. “End” muestra mensaje y pone flag de fin
- **Quick test**: puedes repetir sin reiniciar el servidor.
- **Errores típicos**: no aparece → coalición incorrecta.

## Receta 05 — Contador de objetivos (destruye 3)

- **Objetivo**: condición de victoria simple.
- **Ingredientes**: 3 grupos objetivo + flags.
- **Pasos**:
  1. Cada objetivo destruido incrementa un flag contador
  2. Al llegar a 3 → “Success” + fin
- **Quick test**: progresión visible al destruir.
- **Errores típicos**: condición mal (group dead) → revisa grupos.

