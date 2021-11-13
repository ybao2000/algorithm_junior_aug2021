# a = int(input())
# b = int(input())

def gcd(a, b):  # greatest commmon divisor 64, 36 => 4
  if b == 0: 
    return a
  else:
    return gcd(b, a%b)

def lcm_bf(a, b):  # least common multiple 64, 36 => 64 * 9 = 576, 4 * 576 = 64 * 36
  c = max(a, b)
  while True:
    if c % a == 0 and c % b == 0:
      return c
    c += 1

def lcm_euclidean(a, b):
  return a * b // gcd(a, b) # gcd * lcm = a * b

print(lcm_euclidean(6400002, 36030304))