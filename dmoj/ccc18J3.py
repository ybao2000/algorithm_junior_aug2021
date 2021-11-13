a = [int(val) for val in input().split()]
# convert them into coords
coords = [0, 0, 0, 0, 0]
for i in range(1, 5):
  coords[i] = coords[i-1] + a[i-1]

for i in range(5):
  diffs = []  # save them into a list before I print
  for j in range(5):
    diffs.append(abs(coords[i]-coords[j]))
  print(*diffs)