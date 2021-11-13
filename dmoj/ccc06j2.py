m = int(input())
n = int(input())
ways = 0  # initialize the answer to 0
for i in range(1, m+1): # start from 1, end at m (inclusive)
  for j in range(1, n+1): 
    if i + j == 10:
      ways += 1

if ways == 1:
  print("There is 1 way to get the sum 10.")
else:
  print(f"There are {ways} ways to get the sum 10.")
