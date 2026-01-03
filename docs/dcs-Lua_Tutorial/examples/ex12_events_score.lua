local score = { kills = 0 }

world.addEventHandler({
  onEvent = function(self, event)
    if event.id == world.event.S_EVENT_KILL then
      score.kills = score.kills + 1
      trigger.action.outText("Kills: " .. score.kills, 5)
      env.info("[DCS-Lua-Tutorial] kills=" .. score.kills)
    end
  end
})

trigger.action.outText("ex12: scoreboard listo (esperando kills)", 10)

