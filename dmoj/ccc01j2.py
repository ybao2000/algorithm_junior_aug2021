x = int(input())
m = int(input())
for n in range(1, m):
  if x * n % m == 1:  # you found it!
    print(n)
    break
else: # you didn't find it
  print("No such integer exists.")