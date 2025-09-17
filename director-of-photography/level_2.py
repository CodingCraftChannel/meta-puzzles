def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  count = 0
  actors = []
  # Prefix sums: store number of photographers and backdrops seen so far
  photographers_before_pos = [0]
  backdrops_before_pos = [0]

  photographer_count = 0
  backdrop_count = 0

  for i in range(N):
    if C[i] == 'A':
      actors.append(i)
    elif C[i] == 'P':
      photographer_count += 1
    elif C[i] == 'B':
      backdrop_count += 1
    # Append current totals to prefix arrays
    photographers_before_pos.append(photographer_count)
    backdrops_before_pos.append(backdrop_count)
  # For each actor, count valid P and B on both sides within distance [X, Y]
  for a in actors:
    left_start = max(0, a - Y)
    left_end = max(0, a - X + 1)

    right_start = min(N, a + X)
    right_end = min(N, a + Y + 1)
    # Count valid P-A-B arrangements
    count += (photographers_before_pos[left_end] - photographers_before_pos[left_start]) * (backdrops_before_pos[right_end] - backdrops_before_pos[right_start])
    # Count valid B-A-P arrangements
    count += (backdrops_before_pos[left_end] - backdrops_before_pos[left_start]) * (photographers_before_pos[right_end] - photographers_before_pos[right_start])

  return count

if __name__ == '__main__':
  samples = [
    (5, 'APABA', 1, 2, 1),
    (5, 'APABA', 2, 3, 0),
    (8, '.PBAAP.B', 1, 3, 3),
  ]

  for n, c, x, y, expected in samples:
    result = getArtisticPhotographCount(n, c, x, y)
    if result == expected:
      print(f"OK: input=({n}, {c}, {x}, {y})")
    else:
      print(f"FAILED: input=({n}, {c}, {x}, {y}), got={result}, expected={expected}")
