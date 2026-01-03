local altitude = 2500
local text = string.format("Altitud actual (ejemplo): %d ft", altitude)

trigger.action.outText(text, 10)
env.info("[DCS-Lua-Tutorial] " .. text)

