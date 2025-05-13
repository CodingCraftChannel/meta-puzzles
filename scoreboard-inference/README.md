# Scoreboard Inference – Meta Puzzle

This puzzle comes from Meta's official interview question set.

---

## 📘 Problem Summary

You are given the scores of N competitors. Each score is the sum of some subset of problems they solved. Each problem is worth a fixed point value:

- **Level 1**: Each problem is worth **1 or 2** points.
- **Level 2**: Each problem is worth **1, 2, or 3** points.

Your task is to determine the **minimum number of problems** that could produce all the observed scores.

---

## 📺 Related Video
Watch the full explanation on [CodingCraft YouTube Channel](https://www.youtube.com/@CodingCraftChannel)

---

## 💡 Files

- [`level_1.py`](level_1.py): Uses as many 2-point problems as needed; adds one 1-point problem if any score is odd.
- [`level_2.py`](level_2.py): Uses as many 3-point problems as possible; adjusts for 1- or 2-point needs using remainder logic and a small optimization.
