a, b = input().split()
c, d = input().split()
t = int(input())
dist = abs(int(a)-int(c)) + abs(int(b)-int(d))
if dist > t or dist % 2 != t % 2:
  print("N")
else:
  print("Y")