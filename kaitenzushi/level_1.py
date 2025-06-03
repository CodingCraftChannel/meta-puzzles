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
