dollars = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
n = int(input())
for _ in range(n):
  a = int(input())
  dollars[a-1] = 0  # don't forget the offset
offer = int(input())
avg = sum(dollars)/(10-n)
if offer > avg:
  print("deal")
else:
  print("no deal")