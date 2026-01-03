local groupName = "TGT_01"
local group = Group.getByName(groupName)

if not group then
  trigger.action.outText("No existe el grupo: " .. groupName, 10)
  env.info("[DCS-Lua-Tutorial] group not found: " .. groupName)
  return
end

trigger.action.outText("Grupo encontrado: " .. groupName, 10)
env.info("[DCS-Lua-Tutorial] group found: " .. groupName)

