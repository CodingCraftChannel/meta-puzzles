from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  max_score = max(S)
  threes = max_score // 3

  if max_score % 3 == 0:
    return threes + any(s % 3 != 0 for s in S)

  # If we don't have 1 or max_num - 1 in S, we can replace one 3 with 2 of 2
  if max_score % 3 == 1 and 1 not in S and max_score - 1 not in S:
    return threes + 1

  return threes + any(s % 3 == 1 for s in S) + any(s % 3 == 2 for s in S)
