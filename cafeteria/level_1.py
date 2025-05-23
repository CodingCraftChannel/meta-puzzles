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
