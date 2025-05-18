from typing import List

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  # Precompute standalone damage for each warrior
  C = [h * d for h, d in zip(H, D)]

  max_damage = 0
  best_warrior = 0

  run = True
  while run:
    run = False
    next_best = best_warrior

    for i in range(N):
      if i == best_warrior:
        continue

      # Total = solo damage + overlap phase where both attack
      damage = C[best_warrior] + C[i] + max(H[best_warrior] * D[i], H[i] * D[best_warrior])

      if damage > max_damage:
        max_damage = damage
        next_best = i
        run = True

    best_warrior = next_best

  return max_damage / B
  
