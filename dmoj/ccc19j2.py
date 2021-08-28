L = int(input())

for _ in range(L):
  vals = input().split()
  N = int(vals[0])
  ch = vals[1]
  print(ch * N) # this is to create a string with repeated ch