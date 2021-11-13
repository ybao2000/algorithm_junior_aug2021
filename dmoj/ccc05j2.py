# not very good, but works for this simple problem
# def count_divisors(n):
#   ic = 0
#   for i in range(1, n+1):
#     if n % i == 0:
#       ic += 1
#   return ic

def count_divisors(n):
  # 1 and n are divisors for sure
  ic = 2
  k = 2 # k is our iterator
  while k*k <= n: # we are going to stop k when its square is n
    # k*k <= n is much better than k<=sqrt(n)
    if n % k == 0:  # k is a divisor
      if k * k == n:  # k is the square root of n
        ic += 1 
      else:
        ic += 2
    # don't forget to increase k
    k += 1
  return ic
  
a = int(input())
b = int(input())
num = 0 # initialize the answer
for i in range(a, b+1): # b is included
  ic = count_divisors(i)
  if ic == 4:
    num += 1
print(f"The number of RSA numbers between {a} and {b} is {num}")