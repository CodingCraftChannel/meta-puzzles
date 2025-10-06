# Portals – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

You’re placed in a **grid of cells** with `R` rows and `C` columns.  
Each cell contains one of the following characters:

| Symbol | Meaning |
|:--:|:--|
| `.` | Empty cell |
| `S` | Starting position (exactly one) |
| `E` | Exit (at least one) |
| `#` | Wall (cannot pass) |
| `a`–`z` | Portal – teleport between all cells marked with the same letter |

Each second, you can:
1. **Walk** to any of the 4 adjacent cells (up, down, left, right), if it’s not a wall.
2. **Teleport** instantly to another cell with the same portal letter.

Goal:  
Find the **minimum number of seconds** required to reach any exit from the start.  
If impossible, return `-1`.

---

## 🔒 Constraints
- `1 ≤ R, C ≤ 50`
- `G[i][j] ∈ {'.', 'S', 'E', '#', 'a'...'z'}`

---

## 📋 Samples

| # | Grid | Expected |
|:-:|:--|:--:|
| 1 | `.E.`<br>`.#E`<br>`.S#` | **4** |
| 2 | `a.Sa`<br>`####`<br>`Eb.b` | **-1** |
| 3 | `aS.b`<br>`####`<br>`Eb.a` | **4** |
| 4 | `xS..x..Ex` | **3** |

---

## ✅ Levels Covered
- **Level 2**: BFS with teleportation (efficient single-pass over grid)

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

### Key Idea

Use **Breadth-First Search (BFS)** to explore all reachable cells in increasing order of time.  
Each move (walk or teleport) costs exactly 1 second.

**Optimization:**  
Each portal letter (a–z) is used only **once** — after teleporting from it the first time,  
we mark it as *consumed* to prevent redundant revisits.  
This ensures overall linear complexity in grid size.

### Algorithm Steps
1. Parse grid to find:
   - The **starting position `S`**
   - A map of **portal letters → list of positions**
2. Initialize BFS queue with the start.
3. For each popped cell `(r, c)`:
   - If it’s an exit → return distance.
   - Enqueue all 4 walk neighbors that aren’t walls.
   - If cell has a portal letter not yet used:
     - Mark that portal as used.
     - Enqueue all same-letter positions (teleports).
4. If BFS ends with no exit found → return `-1`.

---

### Correctness

- BFS guarantees the shortest path in an unweighted graph.
- Each teleport edge connects all cells of the same letter in one step.
- Consuming a portal after first expansion prevents exponential branching.

---

### Complexity
- **Time:** `O(R × C)` — every cell processed once; each portal letter expanded once.  
- **Space:** `O(R × C)` for the visited grid and portal map.

---

## 💡 Files
- [`level_2.py`](level_2.py): Final optimized BFS solution with single-use teleport expansion.

---

**Author:** [CodingCraft Channel](https://www.youtube.com/@CodingCraftChannel)
