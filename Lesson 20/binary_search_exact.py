N = int(input())
a = [int(val) for val in input().split()]
target = int(input())

# assume a is sorted
# find the target (exact)
# return the index, if not found, return -1
def binary_search():
  l, r = 0, N-1 # initialize l, r
  while  l<=r:  # while l <= r
    mid = (l+r)//2  # calculate the mid
    if a[mid] == target:  # check the value of mid with the target
      return mid
    elif a[mid] < target:
      l = mid + 1
    else:
      r = mid -1
  else:
    return -1

print(binary_search())
