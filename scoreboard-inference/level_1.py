from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
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

if __name__ == '__main__':
  samples = [
    (6, [1, 2, 3, 4, 5, 6], 4),
    (4, [4, 3, 3, 4], 3),
    (4, [2, 4, 6, 8], 4),
  ]

  for n, s, expected in samples:
    result = getMinProblemCount(n, s)
    if result == expected:
      print(f"OK: input=({n}, {s})")
    else:
      print(f"FAILED: input=({n}, {s}), got={result}, expected={expected}")
