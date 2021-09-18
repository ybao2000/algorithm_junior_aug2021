n = int(input())
line = input()
letters = set()
for ch in line:
  letters.add(ch.lower())

if len(letters) == 26:
  print("YES")
else:
  print("NO")