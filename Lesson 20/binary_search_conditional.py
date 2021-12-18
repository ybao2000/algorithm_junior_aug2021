N = int(input())
a = [int(val) for val in input().split()]
target = int(input())

# assume a is sorted
# find the first value >= target
def binary_search():
  l, r = 0, N-1
  ans = -1  # need auxiliary variable
  while l <= r:
    mid = (l+r)//2
    if a[mid] >= target:
      ans = mid
      r = mid - 1
    else:
      l = mid + 1
  return ans

print(binary_search())