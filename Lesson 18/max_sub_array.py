a = [3, -4, 2, -1, 4, 5, -2, -3, 7, -2, -5]

# find the sub array which has the max sum
# brute force O(n^3)
max_sum = 0
for i in range(len(a)):
  for j in range(i, len(a)):
    s = 0
    for k in range(i, j+1):
      s += a[k]

    if s > max_sum:
      max_sum = s
print(max_sum)