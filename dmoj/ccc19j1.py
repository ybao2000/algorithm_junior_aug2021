A3 = int(input())
A2 = int(input())
A1 = int(input())
B3 = int(input())
B2 = int(input())
B1 = int(input())
total_A = A3 * 3 + A2 * 2 + A1
total_B = B3 * 3 + B2 * 2 + B1

if total_A > total_B:
  print("A")
elif total_A < total_B:
  print("B")
else:
  print("T")