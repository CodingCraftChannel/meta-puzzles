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
