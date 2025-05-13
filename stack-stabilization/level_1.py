from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  count = 0
  prev_disk_size = R[-1]

  for i in range(N - 1, 0, -1):
      if R[i] <= i:
          return -1
        
      if R[i - 1] >= prev_disk_size:
          count += 1
          prev_disk_size = prev_disk_size - 1
      else:
          prev_disk_size = R[i - 1]

  return count
