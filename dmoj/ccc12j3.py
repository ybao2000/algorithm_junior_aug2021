a = "*x*"
b = " xx"
c = "* *"

n = int(input())
for _ in range(n):  # repeat n times
  for x in a:
    print(x*n, end='')  # don't go to next line
  print() # next line

for _ in range(n):  # repeat n times
  for x in b:
    print(x*n, end='')  # don't go to next line
  print() # next line

for _ in range(n):  # repeat n times
  for x in c:
    print(x*n, end='')  # don't go to next line
  print() # next line