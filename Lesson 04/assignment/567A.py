n = int(input())
numbers = [int(val) for val in input().split()]
for i in range(n):
  if i == 0:
    diff_min = numbers[i+1]-numbers[i]
    diff_max = numbers[n-1]-numbers[i]
  elif i==n-1:
    diff_min = numbers[i]-numbers[i-1]
    diff_max = numbers[i]-numbers[0]
  else:
    diff_min = min(numbers[i]-numbers[i-1], numbers[i+1]-numbers[i])
    diff_max = max(numbers[i]-numbers[0], numbers[n-1]-numbers[i])
  print(diff_min, diff_max)