local function say(text, seconds)
  trigger.action.outText(text, seconds or 10)
end

local function log(text)
  env.info("[MyMission] " .. text)
end

local function getFlag(flagName)
  return trigger.misc.getUserFlag(tostring(flagName))
end

local function scheduleEvery(seconds, fn)
  local function runner()
    fn()
    return timer.getTime() + seconds
  end
  timer.scheduleFunction(function()
    return runner()
  end, nil, timer.getTime() + seconds)
end

say("ex15: recetas cargadas", 10)
log("recipes loaded, flag1=" .. getFlag(1))

scheduleEvery(10, function()
  log("tick 10s")
end)

