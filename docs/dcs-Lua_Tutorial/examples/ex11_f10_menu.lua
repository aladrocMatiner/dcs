local menu = missionCommands.addSubMenu("Tutorial Lua")

missionCommands.addCommand("Decir hola", menu, function()
  trigger.action.outText("Hola desde el menú F10", 10)
end)

