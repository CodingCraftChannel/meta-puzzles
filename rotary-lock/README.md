# Rotary Lock – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

You're given a circular lock with numbers `1` to `N`.  
A code is a sequence of `M` numbers you need to enter in order.

- **Level 1**: One wheel, starts at 1
- **Level 2**: Two wheels, both start at 1; for each number, choose which wheel to rotate

Moving 1 unit clockwise or counter-clockwise takes 1 second.  
Selecting a number takes no time.

---

## ✅ Levels Covered
- **Level 1**: Greedy single wheel movement
- **Level 2**: Dynamic programming with state tracking for both wheels

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 💡 Files

- [`level_1.py`](level_1.py): Simple greedy solution for one wheel
- [`level_2.py`](level_2.py): Two-wheel optimization using dynamic programming
