n = int(input())
total = 0
for _ in range(n):
  vals = input().split()
  c1 = int(vals[0])
  c2 = int(vals[1])
  c3 = int(vals[2])
  if c1+c2+c3 >= 2:
    total += 1
print(total)
