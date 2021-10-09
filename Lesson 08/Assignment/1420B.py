t = int(input())
for _ in range(t):
  n = int(input())
  nums = [int(val) for val in input().split()]
  total = 0
  repo = {}
  for num in nums:
    b = len(bin(num)[2:])
    if b in repo:
      repo[b] += 1
    else:
      repo[b] = 1
  for val in repo.values():
    total += val * (val-1) // 2
  print(total)