a = [3, -4, 2, -1, 4, 5, -2, -3, 7, -2, -5]

# find the sub array which has the max sum
# brute force O(n^2)
max_sum = 0
for i in range(len(a)):
  s = 0
  for j in range(i, len(a)):
    s += a[j]
    if s > max_sum:
      max_sum = s

print(max_sum)