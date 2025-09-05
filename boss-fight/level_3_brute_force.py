from typing import List

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  idx = list(range(N))
  byH = sorted(idx, key=lambda i: (-H[i], -D[i]))
  byD = sorted(idx, key=lambda i: (-D[i], -H[i]))
  max_damage = 0
  maxD_so_far = 0

  for i in range(N):
    front_idx = byH[i]
    front_H, front_D = H[front_idx], D[front_idx]

    if front_D <= maxD_so_far:
      continue

    maxD_so_far = front_D

    maxH_so_far = 0
    for j in range(N):
      back_idx = byD[j]
      back_H, back_D = H[back_idx], D[back_idx]

      if back_idx == front_idx:
        continue
      if back_H <= maxH_so_far:
        continue

      maxH_so_far = back_H
      base = front_H * front_D + back_H * back_D
      cross = max(front_H * back_D, back_H * front_D)
      max_damage = max(max_damage, base + cross)

  return max_damage / B
