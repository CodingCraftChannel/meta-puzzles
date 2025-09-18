from typing import List
import queue

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  eaten_set = set()
  eaten_list = queue.Queue()
  count = 0
  
  for i in range(N):
    if D[i] not in eaten_set:
      count += 1
      eaten_set.add(D[i])
      eaten_list.put(D[i])
      
      if len(eaten_set) > K:
        eaten_set.remove(eaten_list.get())
  
  return count

if __name__ == '__main__':
  samples = [
    (6, [1, 2, 3, 3, 2, 1], 1, 5),
    (6, [1, 2, 3, 3, 2, 1], 2, 4),
    (7, [1, 2, 1, 2, 1, 2, 1], 2, 2),
  ]

  for n, d, k, expected in samples:
    result = getMaximumEatenDishCount(n, d, k)
    if result == expected:
      print(f"OK: input=({n}, {d}, {k})")
    else:
      print(f"FAILED: input=({n}, {d}, {k}), got={result}, expected={expected}")
