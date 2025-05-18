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
- **Level 3**: Efficient greedy refinement – handles `N ≤ 500,000` in practice, despite theoretical O(N²)

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

### Explanation

Despite the worst-case time complexity of **O(N²)**, this algorithm usually finds the correct solution in **O(N)**.  
We can make really good guesses about the best warriors simply by:
- Picking a random warrior `A`
- Finding the best warrior `B` to partner with `A`
- Repeating the process with `B` to find `C`, and so on  
until the total damage no longer improves.

This solution uses a greedy iterative strategy:
- Tracks a "best front-line warrior"
- Iteratively tests all possible backups
- Quickly converges to an optimal or near-optimal pair

Time Complexity: Practically close to **O(N)**  
Space Complexity: **O(N)** (for precomputed damage array)

---

## 💡 Files

- [`level_3.py`](level_3.py): Optimized greedy solution
