# Kaitenzushi – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

You are at a Kaitenzushi restaurant with a row of `N` dishes passing one by one on a belt.  
Each dish has a type `D[i]`. You love variety and will only eat a dish if you haven’t eaten the same type in the last `K` dishes.

> You eat each eligible dish instantly before the next one arrives.

**Goal:**  
Determine the **maximum number of dishes** you will eat — while never repeating the same dish type within the last `K` eaten dishes.

---

## 🔒 Constraints

- `1 ≤ N ≤ 500,000`  
- `1 ≤ K ≤ N`  
- `1 ≤ D[i] ≤ 1,000,000`

---

## ✅ Levels Covered

- **Level 1**: Efficiently manage a rolling memory of size `K` to track recently eaten dish types

---

## 📺 Related Video

Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

### Explanation

To avoid eating the same type within the last `K` dishes, we need to:
- Track the **types of the last `K` eaten dishes**
- For each new dish:
  - If it’s not in the recent list, eat it and update memory
  - Otherwise, skip it

We use:
- A `queue` to keep the order of recently eaten dishes
- A `set` to check for duplicates in O(1)

### Time Complexity:
- **O(N)** — one pass through the list, constant-time updates

### Space Complexity:
- **O(K)** for the queue and set used to track recent dish types

---

## 💡 Files

- [`level_1.py`](level_1.py): Sliding window solution using queue + set
