n = int(input())
a = 100
b = 100
for _ in range(n):
  vals = input().split()
  x = int(vals[0])
  y = int(vals[1])
  if x > y:
    b -= x
  elif x < y:
    a -= y
print(a)
print(b)
