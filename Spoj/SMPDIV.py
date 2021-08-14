t = int(input())
for _ in range(t):
  vals = input().split()
  n = int(vals[0])
  x = int(vals[1])
  y = int(vals[2])
  res = []
  for i in range(2, n):
    if i % x == 0 and i % y > 0:
      res.append(i)
  print(*res)