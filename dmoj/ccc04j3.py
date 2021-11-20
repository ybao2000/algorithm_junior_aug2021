n = int(input())
m = int(input())
adjs = []
nouns = []
for _ in range(n):
  adjs.append(input())
for _ in range(m):
  nouns.append(input())
for adj in adjs:
  for noun in nouns:
    print(f"{adj} as {noun}")
