squares = []
# going to have list of sub-list
for _ in range(4):
  vals = [int(val) for val in input().split()]
  squares.append(vals)

s = set()
for i in range(4):
  s1 = 0
  s2 = 0
  for j in range(4):
    s1 += squares[i][j]   # for each row, sum up the cells
    s2 += squares[j][i]   # for each column, sum up the cells
  s.add(s1)
  s.add(s2)

if len(s) == 1:
  print("magic")
else:
  print("not magic")