from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  count = 0
  max_allowed = R[-1]           # Start from the bottom disc

  for i in range(N - 1, 0, -1):
    if R[i] <= i:
      return -1                 # Invalid disc size: radius too small
        
    if R[i - 1] >= max_allowed:
      count += 1                # Deflate to make strictly decreasing
      max_allowed -= 1
    else:
      max_allowed = R[i - 1]

  return count
