# f(n) = 1*2*3*...n
# f(n) = f(n-1) * n

def fact(n):
  if n == 0:
    return 1
  return fact(n-1)*n

print(fact(5))