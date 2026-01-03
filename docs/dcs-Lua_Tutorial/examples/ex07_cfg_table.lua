local CFG = {
  messageDuration = 10,
  welcome = "Bienvenido al entrenamiento",
}

trigger.action.outText(CFG.welcome, CFG.messageDuration)
env.info(string.format("[DCS-Lua-Tutorial] CFG.messageDuration=%d", CFG.messageDuration))

