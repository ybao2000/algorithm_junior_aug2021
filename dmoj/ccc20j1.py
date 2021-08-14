S = int(input())
M = int(input())
L = int(input())

total = S + 2 * M + 3 * L
if total < 10:
  print("sad")
else:
  print("happy")