from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  count = 0
  max_allowed = R[-1]           # Start from the bottom disc

  for i in range(N - 1, 0, -1):
    if R[i] <= i:
      return -1                 # Invalid disc size: radius too small
        
    if R[i - 1] >= max_allowed:
      count += 1                # Deflate to make strictly decreasing
      max_allowed -= 1
    else:
      max_allowed = R[i - 1]

  return count

if __name__ == '__main__':
  samples = [
    (5, [2, 5, 3, 6, 5], 3),
    (3, [100, 100, 100], 2),
    (4, [6, 5, 4, 3], -1),
  ]

  for n, s, expected in samples:
    result = getMinimumDeflatedDiscCount(n, s)
    if result == expected:
      print(f"OK: input=({n}, {s})")
    else:
      print(f"FAILED: input=({n}, {s}), got={result}, expected={expected}")
