N = int(input())
k = int(input())
total = N
for _ in range(k):
  N = N * 10
  total += N

print(total)