# def add_up(n):
#   # calculate 1+2+3+...+n
#   total = 0
#   for i in range(1, n+1):
#     total += i
#   return total

def add_up(n):
  if n == 1:
    return 1
  return add_up(n-1)+n

print(add_up(100))