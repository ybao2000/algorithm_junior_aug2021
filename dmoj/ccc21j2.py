N = int(input())

# use iterations/loops
highest_bid = 0 # init the highest bid as 0
for _ in range(N):
  name = input()
  amount = int(input())
  if amount > highest_bid:
    winner = name
    highest_bid = amount

print(winner)
