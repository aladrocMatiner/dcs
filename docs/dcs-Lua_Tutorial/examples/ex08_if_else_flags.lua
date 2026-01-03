local flagName = "1"
local value = trigger.misc.getUserFlag(flagName)

if value == 1 then
  trigger.action.outText("Flag 1 = 1 (modo entrenamiento ON)", 10)
else
  trigger.action.outText("Flag 1 ≠ 1 (modo entrenamiento OFF)", 10)
end

