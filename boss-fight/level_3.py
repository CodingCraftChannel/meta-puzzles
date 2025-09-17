from typing import List

class LiChaoMax:
  """
  Li Chao segment tree for maximum of lines y = m*x + b over x in [X_MIN, X_MAX].
  """
  class Line:
    __slots__ = ("m", "b")
    def __init__(self, m: int, b: int):
      self.m, self.b = m, b
    def value(self, x: int) -> int:
      return self.m * x + self.b

  class Node:
    __slots__ = ("l", "r", "line")
    def __init__(self):
      self.l, self.r, self.line = None, None, None

  def __init__(self, x_min: int, x_max: int):
    self.X_MIN, self.X_MAX, self.root = x_min, x_max, self.Node()

  def _add_line(self, node, new_line, l: int, r: int):
    mid = (l + r) // 2
    if node.line is None:
      node.line = new_line
      return
    left_is_better = new_line.value(l) > node.line.value(l)
    mid_is_better  = new_line.value(mid) > node.line.value(mid)
    right_is_better = new_line.value(r) > node.line.value(r)

    # Keep the better line at mid
    if mid_is_better:
      node.line, new_line = new_line, node.line

    if l == r:
      return

    if left_is_better != mid_is_better:
      if node.l is None:
        node.l = self.Node()
      self._add_line(node.l, new_line, l, mid)
    elif right_is_better != mid_is_better:
      if node.r is None:
        node.r = self.Node()
      self._add_line(node.r, new_line, mid + 1, r)

  def add_line(self, m: int, b: int):
    self._add_line(self.root, self.Line(m, b), self.X_MIN, self.X_MAX)

  def _query(self, node, x: int, l: int, r: int) -> int:
    if node is None or node.line is None:
      return -10**100  # effectively -inf for our domain
    res = node.line.value(x)
    if l == r:
      return res
    mid = (l + r) // 2
    if x <= mid:
      return max(res, self._query(node.l, x, l, mid))
    else:
      return max(res, self._query(node.r, x, mid + 1, r))

  def query(self, x: int) -> int:
    return self._query(self.root, x, self.X_MIN, self.X_MAX)

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  # Domain for x is health values; constraints say 1..1e9
  X_MIN, X_MAX = 1, 10**9

  # Helper to run a scan with j from a moving set (either left of i or right of i)
  def scan(values_from: range) -> List[int]:
    lichao = LiChaoMax(X_MIN, X_MAX)
    best = [-(10**100)] * N
    for idx in values_from:
      x = H[idx]
      # Query current structure (built from earlier indices in this scan)
      best[idx] = lichao.query(x)
      # Add line for current warrior j: y = D_j * x + D_j * H_j
      lichao.add_line(D[idx], D[idx] * H[idx])
    return best

  # Left-to-right: for each i, consider j < i
  best_left = scan(range(N))
  # Right-to-left: for each i, consider j > i
  best_right = scan(range(N-1, -1, -1))

  ans_num = 0  # numerator before dividing by B
  NEG_INF = -(10**90)

  for i in range(N):
    # best j excluding i:
    best_j = max(best_left[i], best_right[i])
    if best_j == NEG_INF:
      continue
    # total numerator: H_i*D_i + best_j
    total = H[i] * D[i] + best_j
    if total > ans_num:
      ans_num = total

  return ans_num / B

if __name__ == '__main__':
  samples = [
    (3, [2, 1, 4], [3, 1, 2], 4, 6.5),
    (4, [1, 1, 2, 100], [1, 2, 1, 3], 8, 62.75),
    (4, [1, 1, 2, 3], [1, 2, 1, 100], 8, 62.75),
    (4, [16, 8, 12, 11], [5, 16, 12, 14], 1, 466),
  ]

  for n, h, d, b, expected in samples:
    result = getMaxDamageDealt(n, h, d, b)
    if result == expected:
      print(f"OK: input=({n}, {h}, {d}, {b})")
    else:
      print(f"FAILED: input=({n}, {h}, {d}, {b}), got={result}, expected={expected}")
