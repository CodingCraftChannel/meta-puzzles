from typing import List

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  if S == 0.0:
    total = float(sum(V))
    return total - C if total > C else 0.0
  if S == 1.0:
    return sum(max(0.0, float(x) - C) for x in V)

  survive = 1.0 - S
  states = [(0.0, 0.0)]
  best = 0.0
  
  for day in range(N):
    next_states = []
    for profit, stash in states:
      take_profit = profit + V[day] + stash - C
      if take_profit > best:
        next_states.append((take_profit, 0.0))
        best = take_profit
      next_stash = (stash + V[day]) * survive
      if (profit + next_stash) < best:
        continue
      next_states.append((profit, next_stash))
    states = next_states

  return best
