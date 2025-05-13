# Task Rabbit Hole – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

You're exploring an online encyclopedia made up of `N` web pages, where each page contains a single link to another page. Every page `i` links to page `L[i]`, with no self-loops allowed.

You can start your session on any page, and during your session, you may either follow the link from the current page or stop browsing. You cannot visit the same page more than once in a single session.

The goal is to determine the **maximum number of unique pages** you can visit in one session, starting from any page and stopping at any point.

---

## ✅ Levels Covered

- **Level 2** – Efficient DFS-based solution using traversal ID and cycle detection

---

## 📺 Related Video

Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 💡 Files

- [`level_2.py`](level_2.py) – Efficient solution using functional graph traversal with cycle detection and memoization

---

## 🧩 Level 2: Maximum Visitable Pages

**Description:**  
Each of the `N` web pages links to a different page. You can start at any page, and at each step either stop or click the link to the next page. Pages may form chains or cycles, and you cannot visit the same page more than once in a session.

**Objective:**  
Return the **maximum number of distinct pages** you can visit in a single session.

**Constraints:**
- 2 ≤ N ≤ 500,000  
- 1 ≤ L[i] ≤ N  
- L[i] ≠ i

**Approach:**  
The problem is modeled as a **functional graph** (one outgoing edge per node).  
The solution uses a DFS-like traversal with unique traversal IDs to detect cycles and reuse previously computed results. When a cycle is detected, its length is assigned to all nodes within it. For acyclic paths, memoized path lengths are extended backward during the unwind phase to assign the maximum visitable page count per start node. The final result is the maximum value across all starting nodes.
