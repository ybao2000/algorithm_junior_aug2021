# 1x1=1
# 2x1=2 2x2=4
# 3x1=3 3x2=6
#...
# 9x1=9 9x2=18
for row in range(1, 10):
  for col in range(1, row+1):
    result = row * col
    print(f"{row}x{col}={result:2d}", end=" ")
  print() # end line