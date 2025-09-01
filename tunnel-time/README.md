# Tunnel Time – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

A train runs clockwise at **1 m/s** on a **circular track** of circumference `C`.
There are `N` disjoint tunnels covering open intervals **[A<sub>i</sub>, B<sub>i</sub>]** on the track (none includes/touches position `0`, and no two tunnels touch or overlap).

**Tunnel time** is the total number of seconds the train has spent inside tunnels so far.
Goal: find the earliest time t (seconds) when tunnel time first reaches K.

**Goal:**  
Find the earliest **time** `t` **(seconds)** when tunnel time first reaches `K`.

---

## 🔒 Constraints
- `3 ≤ C ≤ 1e12`
- `1 ≤ N ≤ 500,000`
- `1 ≤ A[i] < B[i] ≤ C-1`
- Tunnels are **disjoint** and **don’t touch** each other or `0`
- `1 ≤ K ≤ 1e12`
- Each test is formulated so the correct answer `t ≤ 1e15`

---

## 📋 Samples
- Case 1: `C=10, N=2, A=[1,6], B=[3,7], K=7` → `22`
- Case 2: `C=50, N=3, A=[39,19,28], B=[49,27,35], K=15` → `35`

---

## ✅ Levels Covered
- **Level 2**: Arithmetic fast-forward + single-lap scan (passes Meta limits comfortably)

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 🧠 Solution Summary

### Key Idea

- Let `L = Σ(B[i] − A[i])` be tunnel seconds per **one full lap**.
- Compute `full_laps, remainder = divmod(K, L)`:
  - After `full_laps laps`, tunnel time is `full_laps * L` and wall time is `full_laps * C`.
  - If `remainder == 0`, we stop **at the end of the last tunnel** of lap `full_laps`:
    - **Answer**: `t = (full_laps - 1) * C + lastB`
  - Otherwise, scan the tunnels of the **next lap** in order, subtracting segment lengths until the `remainder` lands inside some tunnel `[a, b]`.

    If after subtracting we have `remainder ≤ 0`, we’re `|remainder|` meters from `b`, i.e. at position `b + remainder`.

    **Answer**: `t = full_laps * C + (b + remainder)`

This avoids simulating many laps: we “fast-forward” using simple arithmetic, then finish within at most one lap.

### Correctness (sketch)

- The train’s tunnel time increases at rate 1 exactly when inside tunnels; per lap that totals `L` seconds.
- By Euclidean division `K= full_laps * L + remainder`, the earliest time to hit `K` occurs:
 - at the **end of a tunnel** if `remainder == 0`, or
 - **inside** a specific tunnel where the `remainder`-th tunnel second of the next lap occurs.
- Disjoint, non-touching intervals ensure a strictly increasing order and a unique stop point.

### Complexity

- **Time:** `O(N log N)` (sort intervals by start) + `O(N)` (worst-case single-lap scan)
- **Space:** `O(N)` to hold intervals (no extra heavy structures)

---

## 💡 Files

- [`level_2.py`](level_2.py): Final solution (fast-forward by laps, then single-lap scan)
