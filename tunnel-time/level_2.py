from typing import List

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  intervals = sorted(zip(A, B))         # sort by A
  L = sum(b - a for a, b in intervals)  # tunnel seconds per lap
  full_laps, remainder = divmod(K, L)
  lastB = intervals[-1][1]              # end of last tunnel in a lap
  
  if remainder == 0:
    return lastB + (full_laps - 1) * C
  
  for a, b in intervals:
    remainder -= b - a
    if remainder <= 0:
      return full_laps * C + b + remainder
