T = input()
S = input()

# go through all shifts of S, and check if it is a substring of T
for i in range(len(S)):
  if S in T:
    print("yes")
    break
  S = S[1:] + S[0]  # this is the shift: put the first to the end
else:
  print("no")