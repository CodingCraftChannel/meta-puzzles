# Uniform Integers – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

A positive integer is called **uniform** if all its digits are the same.  
Examples: `1`, `22`, `333`, `9999` — all uniform.  
In contrast, `23` or `121` are not.

**Goal:**  
Given two integers `A` and `B`, determine how many **uniform integers** exist in the inclusive range `[A, B]`.

---

## 🔒 Constraints

- `1 ≤ A ≤ B ≤ 10¹²`

---

## ✅ Levels Covered
- **Level 1**: Brute-force optimized via direct generation of valid uniform numbers

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

### Explanation

We do **not** check each number from `A` to `B`.  
Instead, we **generate only uniform integers** like `1`, `11`, `222`, etc., and count those that fall within `[A, B]`.

Steps:
- Loop through digit lengths from `len(str(A))` to `len(str(B))`
- For each digit (1 to 9), form a uniform number like `digit * length`
- Count how many fall into the given range

### Why It’s Efficient:
Only ~108 uniform integers exist in total (`9 digits × 12 lengths`),  
so the solution runs instantly even for huge ranges.

### Time Complexity:
- **O(1)** practically — bounded by constant iterations
- No iteration over range `[A, B]`

### Space Complexity:
- **O(1)** auxiliary

---

## 💡 Files

- [`level_1.py`](level_1.py): Clean Python implementation using digit-based generation
