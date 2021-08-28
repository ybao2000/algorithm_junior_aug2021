P = int(input())
N = int(input())
R = int(input())

day = 0
recent = N
total = N

while total <= P:
  recent = recent * R
  total += recent   # total = total + recent
  day += 1

print(day)