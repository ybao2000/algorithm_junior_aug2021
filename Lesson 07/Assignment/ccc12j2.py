a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b > a and c > b and d > c:
  print("Fish Rising")
elif b < a and c < b and d < c:
  print("Fish Diving")
elif b == a and c == b and d == c:
  print("Fish At Constant Depth")
else:
  print("No Fish")