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
