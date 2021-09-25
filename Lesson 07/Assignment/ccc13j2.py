line = input()
s = {"I", "O", "S", "H", "Z", "X", "N"}
for ch in line:
  if ch not in s:
    print("NO")
    break
else:
  print("YES")