from typing import List

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  return N - min(P)

if __name__ == '__main__':
  samples = [
    (3, 1, [1], 2),
    (6, 3, [5, 2, 4], 4),
  ]

  for n, f, p, expected in samples:
    result = getSecondsRequired(n, f, p)
    if result == expected:
      print(f"OK: input=({n}, {f}, {p})")
    else:
      print(f"FAILED: input=({n}, {f}, {p}), got={result}, expected={expected}")
