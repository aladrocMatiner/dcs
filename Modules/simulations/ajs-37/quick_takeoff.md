# AJS-37 Viggen — Quick Takeoff (DCS)

Basado en `docs/DCS_AJS37_Flight_Manual_EN.pdf` (capítulo “Takeoff & Landing”).

## Antes de entrar a pista (rápido)

- Avión listo (motor arrancado, generador ON, sistemas básicos estables).
- Configura lo mínimo para despegar y navegar: `Master Mode` y HUD.

## En cabecera (Before take-off)

![Before take-off checklist](docs/quick_takeoff_assets/before_takeoff.png)

1. Alinea el avión con la pista.
2. Comprueba: curso principal, curso backup, horizonte artificial backup y altímetro.
3. `Master Mode selector`: `NAV` (como mínimo 2 minutos antes de dar potencia, para evitar problemas del sistema de navegación).
4. Ajuste manual de curso (si hace falta): una vez alineado cuidadosamente con el rumbo de pista, pulsa el botón `Reference` (en la palanca).
5. `SPAK`: `ON` y comprueba que la luz está encendida.
6. Master Caution / Warning lights: comprobar (la luz `X-TANK BRÄ` suele desaparecer primero tras ~70% RPM).
7. Simbología HUD: comprobar que la información es correcta.
8. Luz de aterrizaje: `LANDNING` (ON).

Nota del manual: el radar y el indicador central (CI) funcionan ~30 s después de poner `Master Mode` en `NAV`, y ~180 s después de tener el generador ON (inicialización).

### Ajuste manual de curso inicial (solo si lo necesitas)

Útil si la pista está deslizante y hay fuerte viento cruzado.

1. `Master Mode selector`: `NAV`.
2. Sube el cristal del HUD a modo “inflight” (arriba).
3. Alinea cuidadosamente el avión con el rumbo de pista.
4. Pulsa `Reference` (en la palanca).
5. Baja el cristal del HUD al modo “takeoff/landing” (abajo).

Para resetear un ajuste manual ya hecho: cicla `Master Mode` `NAV → BER → NAV` (también para forzar ajuste automático del curso inicial).

## Método 1: despegue usando el HUD (recomendado)

![Takeoff using the HUD](docs/quick_takeoff_assets/takeoff_hud_method.png)

1. Frena (`Wheel brakes`).
2. Acelera a potencia máxima SIN postcombustión.
   - Comprueba EGT (máx `590°C + temperatura exterior`).
3. Suelta frenos y mantén eje con pedales.
4. Si hace falta, enciende postcombustión.
   - Comprueba:
     - Indicador de zona = zona deseada.
     - Indicador de tobera = zona alcanzada.
     - EPR (Pressure ratio):
       - Zona 2: `< +15°C` → `> 1.9`
       - Zona 2: `> +15°C` → `> 1.8`
       - Zona 3: potencia máxima.
5. Comprueba IAS y la línea de tiempo/distancia.
6. Rota cuando la línea de tiempo/distancia llegue a las marcas.
   - Coloca el vector de trayectoria (FPV):
     - Sin postcombustión: sobre la línea del horizonte.
     - Con postcombustión: aprox. a la altura de los pilares exteriores (≈ `3°` sobre horizonte).
7. Comprueba que la velocidad sigue aumentando.
8. Tren arriba cuando estés en el aire.
   - Nota: al subir el tren, se retraen flaps y puede haber una ligera pérdida de sustentación.
9. Mantén actitud de ascenso hasta que aparezca el FPV; el HUD debería cambiar automáticamente de simbología de despegue a navegación.
10. Sube el cristal del HUD a modo “inflight” para ver simbología a ángulos de ataque más bajos.

## Método 2: despegue usando el indicador de actitud

![Takeoff using attitude indicator](docs/quick_takeoff_assets/takeoff_attitude_method.png)

1. Pasos 1–4: igual que el método HUD.
2. Rotación:
   - A `280 km/h`: a `10°` de ascenso (potencia máx sin postcombustión).
   - A `250 km/h`: a `13°` de ascenso (con postcombustión).
3. Tren arriba cuando estés en el aire (misma nota sobre flaps/sustentación).
4. Sube el cristal del HUD a modo “inflight” si necesitas la simbología a AoA bajos.

## Recordatorio de seguridad (rápido)

- En pista deslizante + viento cruzado: usa el ajuste manual de curso inicial.
- Si notas “bache” de sustentación al subir tren: no lo fuerces; estabiliza actitud y velocidad.
