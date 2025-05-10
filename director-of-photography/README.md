# Director of Photography – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

You're given a row of `N` cells, each marked with a character:
- `P`: photographer
- `A`: actor
- `B`: backdrop
- `.`: empty

A photograph is artistic if:
- A photographer, actor, and backdrop are placed in that order (P-A-B or B-A-P)
- The actor is between the two
- The distance between photographer and actor, and actor and backdrop, is within `[X, Y]`

---

## ✅ Levels Covered
- **Level 1**: Brute-force with filters – `N ≤ 200`
- **Level 2**: Optimized with prefix sums – `N ≤ 300,000`

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

- Filter actor, photographer, and backdrop positions
- For each actor:
  - Check valid photographers and backdrops within range
  - Use prefix sums to count efficiently (Level 2)

---

## 💡 Files

- `level_1.py`: Straightforward filtered nested loop
- `level_2.py`: Optimized prefix sum solution
