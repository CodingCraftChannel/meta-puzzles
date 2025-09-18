import math
from typing import List

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  if S == 0.0:
    total = float(sum(V))
    return total - C if total > C else 0.0
  if S == 1.0:
    return sum(max(0.0, float(x) - C) for x in V)

  survive = 1.0 - S
  states = [(0.0, 0.0)]  # (profit, stash)
  best = 0.0
  
  for day in range(N):
    next_states = []

    for profit, stash in states:
      # Take: collect everything today, pay C, stash resets
      take_profit = profit + V[day] + stash - C
      if take_profit > best:
        next_states.append((take_profit, 0.0))
        best = take_profit
      # Skip: add today's package; theft may wipe stash
      next_stash = (stash + V[day]) * survive
      if (profit + next_stash) < best:  # prune hopeless states
        continue

      next_states.append((profit, next_stash))

    states = next_states

  return best

if __name__ == '__main__':
  samples = [
    (6, [10, 2, 8, 6, 4], 5, 0.0, 25.0),
    (5, [10, 2, 8, 6, 4], 5, 1.0, 9.0),
    (5, [10, 2, 8, 6, 4], 3, 0.5, 17.0),
    (5, [10, 2, 8, 6, 4], 3, 0.15, 20.10825),
  ]

  for n, v, c, s, expected in samples:
    result = getMaxExpectedProfit(n, v, c, s)
    if math.isclose(result, expected, abs_tol=1e-6):
      print(f"OK: input=({n}, {v}, {c}, {s})")
    else:
      print(f"FAILED: input=({n}, {v}, {c}, {s}), got={result}, expected={expected}")
