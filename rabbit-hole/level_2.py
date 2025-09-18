from typing import List

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    traversal_id = [0] * (N + 1)    # Map of page → unique traversal ID or status marker
    max_visitable = [0] * (N + 1)   # Max number of distinct pages visitable from each node

    for start in range(1, N + 1):
        if traversal_id[start] != 0:
            continue  # already processed

        current = start
        steps = 0

        # Phase 1: Explore path until reaching visited node
        while traversal_id[current] == 0:
            steps += 1
            traversal_id[current] = start        # mark with this run’s ID
            max_visitable[current] = steps       # temporary depth counter
            current = L[current - 1]             # move to linked page

        # Phase 2: Check if a cycle was found within this traversal
        if traversal_id[current] == start:
            # Loop found: calculate its size
            cycle_length = steps - max_visitable[current] + 1

            # Mark all nodes in the cycle with negative ID and set their value
            while traversal_id[current] != -start:
                traversal_id[current] = -start
                max_visitable[current] = cycle_length
                current = L[current - 1]

        else:
            # We reached a node already resolved by another traversal
            # Extend total path length from where we entered
            steps += max_visitable[current]

        # Phase 3: Assign final max_visitable values in reverse order
        current = start
        while traversal_id[current] == start:
            max_visitable[current] = steps
            steps -= 1
            current = L[current - 1]

    return max(max_visitable)

if __name__ == '__main__':
  samples = [
    (4, [4, 1, 2, 1], 4),
    (5, [4, 3, 5, 1, 2], 3),
    (5, [2, 4, 2, 2, 3], 4),
  ]

  for n, l, expected in samples:
    result = getMaxVisitableWebpages(n, l)
    if result == expected:
      print(f"OK: input=({n}, {l})")
    else:
      print(f"FAILED: input=({n}, {l}), got={result}, expected={expected}")
