def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  count = 0

  # Collect the indices of all actors, photographers, and backdrops
  actors = []
  photographers = []
  backdrops = []

  for i in range(N):
    if C[i] == 'A':
      actors.append(i)
    elif C[i] == 'P':
      photographers.append(i)
    elif C[i] == 'B':
      backdrops.append(i)

  # For each actor, check all possible photographer and backdrop combinations
  for a in actors:
    for p in photographers:
      d1 = abs(p - a)
      # Skip if photographer is too close or too far from actor
      if X > d1 or Y < d1:
        continue
      for b in backdrops:
        # Ensure actor is between photographer and backdrop
        if (p - a) * (a - b) > 0:
          d2 = abs(b - a)
          # Count only if backdrop is also within valid distance
          if X <= d2 and d2 <= Y:
            count += 1

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
