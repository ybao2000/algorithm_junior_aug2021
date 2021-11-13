a = 1024245798
b = 1023234629

# brute force doesn't work for big numbers
def gcd_bf(a, b):
  for x in range(min(a, b), 0, -1):
    if a %x == 0 and b % x == 0:
      # you found it!
      return x

# euclidean algorithm
# recursive function
def gcd_euclidean(a, b):
  if b == 0:
    return a
  return gcd_euclidean(b, a%b)

print(gcd_euclidean(a, b))
