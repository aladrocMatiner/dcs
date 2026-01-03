local function say(text, seconds)
  trigger.action.outText(text, seconds or 10)
end

say("ex09: función say() funcionando", 10)

