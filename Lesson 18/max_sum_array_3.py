# kadane's algorithm (simple dp)
# O(n)

# find the sub array which has the max sum
a = [3, -4, 2, -1, 4, 5, -2, -3, 7, -2, -5]
max_sum_all = 0
max_sum_end_current = 0

for i in range(len(a)):
  # the max_sum_end_current should be 
  # either max_sum_end_prev + current or just current
  max_sum_end_current = max(max_sum_end_current+a[i], a[i])
  max_sum_all = max(max_sum_all, max_sum_end_current)

print(max_sum_all)

