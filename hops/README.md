# Hops – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

We have `N` lily pads numbered `1` to `N`, where pad `N` is next to the shore.  
`F` frogs start on **distinct** lily pads (none on pad `N`).

Every second:
- Exactly **one frog** can jump.
- A frog always jumps to the **nearest free pad ahead** of it (possibly multiple pads forward).
- Frogs can jump over other frogs, but **cannot** skip empty lily pads.
- When a frog reaches pad `N`, it leaves for the shore.

All frogs cooperate to minimize the total time for **all** frogs to reach the shore.

**Goal:**  
Return the minimum number of seconds required for all frogs to reach the shore.

**Constraints:**
- `1 ≤ N ≤ 1,000,000,000,000`
- `1 ≤ F ≤ 500,000`
- `1 ≤ P[i] ≤ N - 1` and all `P[i]` are distinct
- Optimized to run in **O(F)**

---

## ✅ Levels Covered
- **Level 2**: Efficient single-pass computation with direct formula

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

### Explanation

Let `m = min(P)` be the smallest (leftmost) occupied pad.

**Lower bound:**  
At most **one frog** can move per second, and after each second the **minimum occupied pad** can increase by **at most 1**.  
Therefore, it takes at least `(N - m)` seconds for the farthest frog to leave.

**Achievability:**  
We can always move frogs so that in each second the minimum occupied pad increases by exactly 1.  
Once it reaches `N`, all frogs have exited.

**Final formula:**
`seconds = N - min(P)`

**Time Complexity:** **O(F)** – single pass to find the smallest pad.  
**Space Complexity:** **O(1)**.

---

## 💡 Files

- [`level_2.py`](level_2.py): Minimal O(F) solution
