# Cafeteria – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

You are given a row of `N` seats in a cafeteria, numbered from `1` to `N`.  
There are already `M` diners seated, each at position `S[i]`.

A strict social distancing rule applies:  
> Each diner must have at least `K` empty seats on both sides  
> (or as many as possible at the edges).

**Goal:**  
Determine the **maximum number of additional diners** that can be seated  
without violating the distancing rule — assuming they cooperate optimally.

---

## 🔒 Constraints

- `1 ≤ N ≤ 10¹⁵`
- `1 ≤ K ≤ N`
- `1 ≤ M ≤ 500,000`
- `1 ≤ S[i] ≤ N` and all `S[i]` are distinct
- The initial configuration already follows all rules

---

## ✅ Levels Covered
- **Level 1**: Greedy interval placement – handles massive `N` using only the gaps between diners

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

### Explanation

We don't need to simulate all `N` seats.

Instead, we:
- Sort existing diners
- Treat each seated diner as "blocking" `K` seats to the left and right
- Find **gaps** between these blocked zones
- In each free segment, greedily place diners `K+1` seats apart

### Key Formula:
  For any gap of size `L`, we can place:  
  ⌊ L / (K + 1) ⌋ new diners

### Edge Segments:
We also check the very beginning (`1` to first blocked seat) and  
the end (`last blocked seat` to `N`) as potential gaps.

### Time Complexity:
- **O(M log M)** for sorting
- **O(M)** for greedy gap filling

### Space Complexity:
- **O(1)** auxiliary (excluding input)

---

## 💡 Files

- [`level_1.py`](level_1.py): Efficient greedy solution for large `N`
