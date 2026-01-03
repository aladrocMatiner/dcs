local function tick()
  trigger.action.outText("ex10: tick (cada 5s)", 2)
  return timer.getTime() + 5
end

timer.scheduleFunction(function()
  return tick()
end, nil, timer.getTime() + 1)

