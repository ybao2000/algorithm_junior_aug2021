a = int(input())
b = int(input())
c = int(input())
n = int(input())
total = 0
for i in range(0, n//a + 1): # iterate from 0 to n//a, fish a
  for j in range(0, n//b + 1):  # fish b
    for k in range(0, n//c + 1):  # fish c
      if i+j+k > 0 and i * a + j * b + k * c <= n:
        # two condictions: 
        # 1: you need at least one fish
        # 2: your total points should be <= n
        print(f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel")
        total += 1

print(f"Number of ways to catch fish: {total}")