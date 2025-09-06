# Boss Fight – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

You are given `N` warriors, where each warrior `i` has:

- `H[i]` — their health (in HP)
- `D[i]` — their damage per second (DPS)

They are fighting a boss who has:

- Infinite health
- A constant damage rate of `B` DPS

Only **two distinct warriors** will fight the boss at any time:
1. The **front-line** warrior fights first until defeated.
2. The **backup** warrior starts attacking immediately and continues after the front-line warrior dies.

> While the front-line warrior is alive, **both** warriors attack simultaneously.  
> Once the front-line dies, the backup continues alone until they also fall.

Each warrior deals damage as long as they are alive. Damage is dealt **continuously**, meaning partial seconds count.

**Goal:**  
Choose two distinct warriors to **maximize the total damage dealt to the boss** before both warriors are defeated.

**Constraints:**
- `2 ≤ N ≤ 500,000`
- `1 ≤ H[i], D[i], B ≤ 1,000,000,000`
- Must return a result with absolute or relative error ≤ 1e-6

---

## ✅ Levels Covered
- **Level 3**:
  - Brute force with pruning — simpler, often fast enough in practice
  - Li Chao segment tree — fully optimized, handles worst-case efficiently

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

We implemented two different approaches for Level 3:

### 1. Brute Force with Pruning (`level_3_brute_force.py`)
- Sort warriors twice: by health (descending) and by damage (descending).  
- Iterate over possible front-line warriors, and for each, prune backup candidates by checking only those that improve health.  
- Compute total damage as: `total = H_front * D_front + H_back * D_back + max(H_front * D_back, H_back * D_front)`.
- Pruning ensures we avoid full O(N²) scanning, making it efficient in practice even for N up to ~5e5, though the theoretical complexity is still `O(N²)` **worst-case**.
- Easy to implement and passes all test cases.

**Complexities:**  
- **Time:** `~O(N log N)` for sorting + pruned iterations (practically efficient, worst-case `O(N²)`)  
- **Space:** `O(N)`

### 2. Optimized Li Chao Segment Tree (`level_3.py`)
- Reformulate the problem as maximizing a linear function over possible health values.  
- The overlap term `max(H_front * D_back, H_back * D_front)` can be represented as lines (`y = m·x + b`) depending on warrior stats.  
- Use a **Li Chao Segment Tree** to maintain maximum values over ranges and query efficiently.  
- This approach ensures guaranteed `O(N log C)` complexity, where `C` is the health range (`≤ 1e9`).

**Complexities:**  
- **Time:** `O(N log C)` (logarithmic factor from segment tree operations)  
- **Space:** `O(N)` (tree storage + warrior stats)

---

### Comparison
- **Brute Force with Pruning**: simpler, easier to code, fast enough in practice.  
- **Li Chao Segment Tree**: fully optimized, handles worst-case scenarios efficiently, more complex to implement.  

---

## 💡 Files

- [`level_3_brute_force.py`](level_3_brute_force.py): Brute force solution with pruning
- [`level_3.py`](level_3.py): Optimized greedy solution
