def gcd(x, y):
  if y == 0:
    return x
  return gcd(y, x%y)

# def gcd(x, y):
#   # how to use while loop?
#   while y > 0:
#     r = x % y
#     x = y
#     y = r
#   return x

a = 64
b = 78

print(gcd(a, b))