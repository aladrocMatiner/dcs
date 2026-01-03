local pilotName = "Piloto"
local attempts = 1
local fuelPercent = 75.0

trigger.action.outText("Hola, " .. pilotName .. ". Intentos: " .. attempts, 10)
env.info(string.format("[DCS-Lua-Tutorial] attempts=%d fuel=%.1f%%", attempts, fuelPercent))

