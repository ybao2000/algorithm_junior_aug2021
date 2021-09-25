squares = []
# going to have list of sub-list
for _ in range(4):
  vals = [int(val) for val in input().split()]
  squares.append(vals)

total = None
for i in range(4):
  s1 = 0
  s2 = 0
  for j in range(4):
    s1 += squares[i][j]
    s2 += squares[j][i]
  if total is None:
    total = s1
  if total != s1 or total != s2:
    print("not magic")
    break
else:
  print("magic")

    

