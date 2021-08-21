vals = input().split()
a = int(vals[0])  # index 0 is the first one
b = int(vals[1])
total = 0 # initialize the total
for x in range(a, b+1): # you need b+1 to include b+1
  total += x * x
print(total)