repo = {1: 1, 2: 1}

def fibo(n):
  # recursive formula:
  # f(n) = f(n-1) + f(n-2)
  if n in repo:
    return repo[n]
  else:
    value = fibo(n-1) + fibo(n-2)
    # memoization: store the intermediate result, 
    # so that next time you don't have to do it again
    repo[n] = value
    return value

print(fibo(10000000000000000000))