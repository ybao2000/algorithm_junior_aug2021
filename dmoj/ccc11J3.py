t1 = int(input())
t2 = int(input())
total = 2
while True:
  t = t1 - t2
  total += 1
  # check if it is to terminate
  if t2 < t:
    break
  t1 = t2
  t2 = t

print(total)