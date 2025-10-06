from typing import List
from collections import defaultdict, deque

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
  ports = defaultdict(list)
  start = None
  for i in range(R):
    for j in range(C):
      ch = G[i][j]
      if 'a' <= ch <= 'z': ports[ch].append((i, j))
      elif ch == 'S': start = (i, j)
  if not start: return -1

  q = deque([(start[0], start[1], 0)])
  seen = {start}
  used = set()  # portal letters already expanded

  while q:
    r, c, d = q.popleft()
    if G[r][c] == 'E': return d
    for nr, nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
      if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != '#' and (nr, nc) not in seen:
        seen.add((nr, nc)); q.append((nr, nc, d+1))
    ch = G[r][c]
    if 'a' <= ch <= 'z' and ch not in used:
      used.add(ch)
      for nr, nc in ports[ch]:
        if (nr, nc) not in seen:
          seen.add((nr, nc)); q.append((nr, nc, d+1))

  return -1

if __name__ == '__main__':
  samples = [
    (3, 3, [['.', 'E', '.'], ['.', '#', 'E'], ['.', 'S', '#']], 4),
    (3, 4, [['a', '.', 'S', 'a'], ['#', '#', '#', '#'], ['E', 'b', '.', 'b']], -1),
    (3, 4, [['a', 'S', '.', 'b'], ['#', '#', '#', '#'], ['E', 'b', '.', 'a']], 4),
    (1, 9, [['x', 'S', '.', '.', 'x', '.', '.', 'E', 'x']], 3),
  ]

  for r, c, g, expected in samples:
    result = getSecondsRequired(r, c, g)
    if result == expected:
      print(f"OK: input=({r}, {c}, {g})")
    else:
      print(f"FAILED: input=({r}, {c}, {g}), got={result}, expected={expected}")
