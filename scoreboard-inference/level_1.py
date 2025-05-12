from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  one_point_problem_count = 0
  two_point_problem_count = 0

  for i in range(N):
    # Estimate how many 2-point problems could make up this score
    two_points = S[i] // 2
    if two_points > two_point_problem_count:
      two_point_problem_count = two_points
    # If the score is odd, we need at least one 1-point problem
    if S[i] % 2 == 1:
      one_point_problem_count = 1

  return one_point_problem_count + two_point_problem_count
