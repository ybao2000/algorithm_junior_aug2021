a = [int(val) for val in input().split()]
# initialize 2D array
b = []
for _ in range(5):
  b.append([0]*5)

for i in range(5):
  for j in range(5):
    if j < i:
      for k in range(j, i):
        b[i][j] += a[k]
        b[j][i] += a[k]

for i in range(5):
  print(*b[i])

