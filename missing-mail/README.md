# Missing Mail – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

Over `N` days, you manage a mail room:

- Day `i`: a package worth `V[i]` may arrive.
- You may enter (pay fee `C`) and collect all packages.
- End of day: with probability `S`, all packages currently inside are stolen.

You know the full delivery schedule in advance, but only observe the room when you enter.

**Goal:**  
Return the **maximum expected profit** = (sum collected) − (visits × `C`) within `1e-6`.

---

## 🔒 Constraints
- `1 ≤ N ≤ 4000`
- `0 ≤ V[i] ≤ 1000`
- `1 ≤ C ≤ 1000`
- `0.0 ≤ S ≤ 1.0`

---

## 📋 Samples
- Case 1: `N=5, V=[10,2,8,6,4], C=5, S=0.0` → `25.00000000`
- Case 2: `N=5, V=[10,2,8,6,4], C=5, S=1.0` → `9.00000000`
- Case 3: `N=5, V=[10,2,8,6,4], C=3, S=0.5` → `17.00000000`
- Case 4: `N=5, V=[10,2,8,6,4], C=3, S=0.15` → `20.10825000`

---

## ✅ Levels Covered
- **Level 2**: Expected-value DP with frontier pruning (passes all Meta tests within the time limit)

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

### Key Idea

Track a small set of candidate states per day:
- State: `(profit, stash)` where
  - `profit` = collected profit so far
  - `stash` = expected value currently in the room (before theft)
- Choices on day `i`:
  - **Take:** `profit += stash + V[i] - C, stash = 0`
  - **Skip:** `stash = (stash + V[i]) * (1 - S)`

### Pruning (what makes it fast)

- Maintain a **global best** `best = max(profit)` seen so far.
- Keep **only** “take” states that improve `best`.
- Discard “skip” states with `profit + stash < best` (they can never overtake the current best).

This preserves optimality while preventing state explosion.

### Complexity

- **Time:** ~O(N²) worst case; much smaller in practice due to pruning
- **Space:** O(N) (only current/next frontiers)

---

## 💡 Files

- [`level_2.py`](level_2.py): Efficient solution using expected-value DP with frontier pruning (passes all Meta tests)
