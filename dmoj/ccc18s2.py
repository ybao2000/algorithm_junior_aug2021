N = int(input())

a = []
for _ in range(N):
  a.append(input().split())

# you need to find the lowest and figure out the rotation
lowest = int(a[0][0])
rotation = 0

if int(a[-1][0]) < lowest:  # bottom left
  lowest = int(a[-1][0])
  rotation = 1  
if int(a[-1][-1]) < lowest:   # bottom right
  lowest = int(a[-1][-1])
  rotation = 2
# you shouldn't use elif
if int(a[0][-1]) < lowest:  # top right
  lowest = int(a[0][-1])
  rotation = 3


for _ in range(rotation):
  # you need to do the rotation
  a = list(zip(*a[::-1]))

for x in a:
  print(*x)