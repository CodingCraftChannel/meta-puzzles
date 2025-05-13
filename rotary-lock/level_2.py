from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Helper function to compute the shortest distance between two positions on the circular lock
  def calcMinDistance(prev, current, maximum):
    direct_move = abs(current - prev)
    return min(direct_move, maximum - direct_move)

  # Initialize DP state: (left_pos, right_pos) → total time
  tree = {(C[0], 1): calcMinDistance(1, C[0], N)}

  for digit in C[1:]:
    next_tree = {}

    for state in tree.keys():
      # Option 1: use the left wheel to move to the digit
      left_state = (digit, state[1])
      left_distance = calcMinDistance(state[0], digit, N)
      if left_state in next_tree:
        next_tree[left_state] = min(tree[state] + left_distance, next_tree[left_state])
      else:
        next_tree[left_state] = tree[state] + left_distance

      # Option 2: use the right wheel to move to the digit
      right_state = (state[0], digit)
      right_distance = calcMinDistance(state[1], digit, N)
      if right_state in next_tree:
        next_tree[right_state] = min(tree[state] + right_distance, next_tree[right_state])
      else:
        next_tree[right_state] = tree[state] + right_distance

    tree = next_tree

  return min(tree.values())
  
