# Stack Stabilization – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

You are given a vertical stack of `N` inflatable discs, where the `i`-th disc from the top has radius `R[i]` inches. The stack is considered **unstable** if any disc has a radius greater than or equal to the disc directly below it.

The goal is to transform the stack into a **strictly decreasing** sequence of radii (from top to bottom), using level-specific operations.

---

## ✅ Levels Covered

- **Level 1** – Greedy solution to count deflation operations (or detect impossibility)  
- **Level 3** – Dynamic programming solution minimizing total time under asymmetric inflate/deflate costs

---

## 📺 Related Video

Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 💡 Files

- [`level_1.py`](level_1.py) – Greedy solution to count deflation operations (or detect impossibility)
- [`level_3.py`](level_3.py) – Dynamic programming solution minimizing total time under asymmetric inflate/deflate costs

---

## 🧩 Level 1: Minimum Deflations

**Description:**  
You can choose any disc and deflate it to any smaller **positive integer** radius (strictly smaller than its current radius). Each such action counts as **one operation**, regardless of how much the radius decreases.

**Objective:**  
Return the **minimum number of deflations** required to stabilize the stack.  
Return `-1` if it is impossible.

**Constraints:**
- 1 ≤ N ≤ 50  
- 1 ≤ R[i] ≤ 1,000,000,000

**Approach:**  
A greedy backward pass ensures that every disc is strictly smaller than the one below, applying a deflation only when necessary. The solution counts the number of required deflations and returns `-1` if the current radius cannot be adjusted to a valid smaller value.

---

## 🧩 Level 3: Minimum Total Time

**Description:**  
You may perform two types of operations:
- **Inflate** any disc by 1 inch (costs `A` seconds, no upper limit)
- **Deflate** any disc by 1 inch (costs `B` seconds, only allowed if resulting radius remains ≥ 1)

**Objective:**  
Return the **minimum total number of seconds** required to stabilize the stack.

**Constraints:**
- 1 ≤ N ≤ 50  
- 1 ≤ R[i] ≤ 1,000,000,000  
- 1 ≤ A, B ≤ 100

**Approach:**  
The problem is solved using dynamic programming with coordinate compression and prefix minimums. The disc radii are transformed to simplify monotonic constraints, and optimal costs are computed using per-disc adjustments for each compressed candidate radius. This solution supports asymmetric cost structures and passes both small and edge-case tests.
