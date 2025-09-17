from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  S.sort()
  result = 0
  prev = 1
  
  for s in S:
    left = prev
    right = s - K - 1
    if left <= right:
      result += (right - left) // (K + 1) + 1
    prev = s + K + 1
  
  if prev <= N:
    result += (N - prev) // (K + 1) + 1
  
  return result

if __name__ == '__main__':
  samples = [
    (10, 1, 2, [2, 6], 3),
    (15, 2, 3, [11, 6, 14], 1),
  ]

  for n, k, m, s, expected in samples:
    result = getMaxAdditionalDinersCount(n, k, m, s)
    if result == expected:
      print(f"OK: input=({n}, {k}, {m}, {s})")
    else:
      print(f"FAILED: input=({n}, {k}, {m}, {s}), got={result}, expected={expected}")
