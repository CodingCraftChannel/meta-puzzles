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

if __name__ == '__main__':
  samples = [
    (10, 2, [1, 6], [3, 7], 7, 22),
    (50, 3, [39, 19, 28], [49, 27, 35], 15, 35),
  ]

  for c, n, a, b, k, expected in samples:
    result = getSecondsElapsed(c, n, a, b, k)
    if result == expected:
      print(f"OK: input=({c}, {n}, {a}, {b}, {k})")
    else:
      print(f"FAILED: input=({c}, {n}, {a}, {b}, {k}), got={result}, expected={expected}")
