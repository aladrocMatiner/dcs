MyMission = MyMission or {}
local M = MyMission

M.CFG = M.CFG or { msgSeconds = 10 }
M.state = M.state or { boots = (M.state and M.state.boots or 0) + 1 }

local function say(text)
  trigger.action.outText(text, M.CFG.msgSeconds)
end

function M.status()
  say("MyMission boots: " .. M.state.boots)
  env.info("[MyMission] status boots=" .. M.state.boots)
end

M.status()

