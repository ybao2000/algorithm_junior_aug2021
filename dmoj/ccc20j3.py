N = int(input())

# x_min = y_min = 1000  # init the min with a super big number
# x_max = y_max = -1000 # init the max with a super small number
x_min = y_min = None
x_max = y_max = None
for _ in range(N):
  vals = input().split(',')
  x = int(vals[0])
  y = int(vals[1])
  if x_min is None:
    x_min = x
    x_max = x
    y_min = y
    y_max = y
  else:
  #you need to check x_min, y_min, x_max, y_max
    x_min = min(x, x_min) # this is to make x_min smaller 
    x_max = max(x, x_max) # this is to make x_max bigger
    y_min = min(y, y_min)
    y_max = max(y, y_max)

print(f"{x_min-1},{y_min-1}")
print(f"{x_max+1},{y_max+1}")
