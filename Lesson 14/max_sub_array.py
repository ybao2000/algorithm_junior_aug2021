a = [3, 4, -5, -3, 1, 11, -16, 25, 26, -5, 10]
# need to find the sub-array with maximum sum

def max_sub_array_bf(a):
  # O(n^2)
  max_sum = 0
  for i in range(0, len(a)):
    sum = 0
    for j in range(i, len(a)):
      sum += a[j]
      if sum > max_sum:
        max_sum = sum
        result_i = i
        result_j = j
  return max_sum, result_i, result_j

# a better is using Kadane's algorithm (DP algorithm)
# O(n)

s, i, j = max_sub_array_bf(a)
print(f"max sum is {s}, start index is {i}, end index is {j}")