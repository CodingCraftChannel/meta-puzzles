def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  res = 0
  
  for size in range(len(str(A)), len(str(B)) + 1):
    for i in range(1, 10):
      num = int(str(i) * size)
      if A <= num <= B:
        res += 1
      elif B < num:
        break
  
  return res

if __name__ == '__main__':
  samples = [
    (75, 300, 5),
    (1, 9, 9),
    (999999999999, 999999999999, 1),
  ]

  for a, b, expected in samples:
    result = getUniformIntegerCountInInterval(a, b)
    if result == expected:
      print(f"OK: input=({a}, {b})")
    else:
      print(f"FAILED: input=({a}, {b}), got={result}, expected={expected}")
