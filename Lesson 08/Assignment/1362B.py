t = int(input())
for _ in range(t):
  n = int(input())
  a = [int(val) for val in input().split()]
  s = set(a)
  # use brute force, try all numbers
  for k in range(1, 1025):
    s2 = set()
    for x in s:
      y = x ^ k # this is the xor in python
      # you can make it quicker by check
      if y in s2: # this means the two sets cannot be the same
        break
      else:
        s2.add(y)
    # you can compare s1 and s2
    if s == s2:  # python use == to set compare
      print(k)
      break
  else:
    print(-1)

