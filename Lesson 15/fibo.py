def fibo(n):
  # please give me the value at position n
  # n = 0, 0
  # n = 1, 1
  # f(n) = f(n-1) + f(n-2)
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return fibo(n-1) + fibo(n-2)

# please write an iteration without recursive
print(fibo(40))