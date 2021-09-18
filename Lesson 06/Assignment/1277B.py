t = int(input())
for _ in range(t):
  n = int(input())
  a = [int(val) for val in input().split()]
  s = set() # you need a set to store all even numbers
  for i in a:
    while i % 2 == 0: # i is even
      s.add(i)
      i = i//2;
  print(len(s))
