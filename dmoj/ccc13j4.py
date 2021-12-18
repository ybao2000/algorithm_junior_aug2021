T = int(input())
C = int(input())
chores = [] # create an empty list
for _ in range(C):
  c = int(input())
  chores.append(c)
chores.sort()
# accumulate and count
# you need 2 auxiliary variables
total = 0 
cnt = 0 # try to avoid using those reserved words
for c in chores:
  total += c
  if total <= T:
    cnt += 1
  else:
    break
print(cnt)

