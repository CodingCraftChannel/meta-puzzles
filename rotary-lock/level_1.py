from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Helper function to calculate the shortest distance between two numbers on a circular lock
  def calcMinDistance(prev, current, maximum):
    # Option 1: direct distance (clockwise or counter-clockwise)
    # Option 2: wrap-around distance (crossing from N to 1 or 1 to N)
    direct_move = abs(current - prev)
    return min(direct_move, maximum - direct_move)

  prev = 1
  count = 0

  for c in C:
    count += calcMinDistance(prev, c, N)
    prev = c

  return count
