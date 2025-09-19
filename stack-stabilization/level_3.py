from typing import List

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
  # Transform radii to simplify stability check
  adjusted = [r - i for i, r in enumerate(R)]

  # Coordinate compression of all possible target radii
  key_radii = {max(1, r) for r in adjusted}
  key_radii = list(key_radii)
  key_radii.sort()

  cost_for_radius = [0] * len(key_radii)

  # For each disc, compute cost to adjust to each key radius
  for r in adjusted:
      for i, key_radius in enumerate(key_radii):
          delta = key_radius - r
          cost = 0
            
          if delta > 0:
              cost = delta * A
          else:
              cost = -delta * B
            
          if i == 0:
              cost_for_radius[0] += cost
          else:
              cost_for_radius[i] = min(cost_for_radius[i-1], cost_for_radius[i] + cost)
        
  return cost_for_radius[-1]

if __name__ == '__main__':
  samples = [
    (5, [2, 5, 3, 6, 5], 1, 1, 5),
    (3, [100, 100, 100], 2, 3, 5),
    (3, [100, 100, 100], 7, 3, 9),
    (4, [6, 5, 4, 3], 10, 1, 19),
    (4, [100, 100, 1, 1], 2, 1, 207),
    (6, [6, 5, 2, 4, 4, 7], 1, 1, 10),
  ]

  for n, r, a, b, expected in samples:
    result = getMinimumSecondsRequired(n, r, a, b)
    if result == expected:
      print(f"OK: input=({n}, {r}, {a}, {b})")
    else:
      print(f"FAILED: input=({n}, {r}, {a}, {b}), got={result}, expected={expected}")
