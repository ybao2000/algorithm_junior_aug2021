m = int(input())
n = int(input())
d = {0: 0, 1:1, 8:8, 6:9, 9:6}  # a dictionary to store the rotated 
total = 0 # initialize the result
for num in range(m, n+1): # n is included
  a = num
  # a is the original number
  # b will be the rotated number
  b = 0
  while a > 0:
    r = a % 10
    a = a // 10
    if r not in d:  # not valid
      break
    else:
      b = b * 10 + d[r]
  else: # all valid
    if num == b:
      total += 1
print(total)
