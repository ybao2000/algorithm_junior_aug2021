N = int(input())
p1 = input()
p2 = input()
total = 0 # initialize the answer
# iterate the strings
for i in range(N):
  c1 = p1[i]
  c2 = p2[i]
  if c1 == "C" and c2 == "C":
    total += 1
print(total)
