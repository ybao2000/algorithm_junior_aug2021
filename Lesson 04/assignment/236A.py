userName = input()
# s = set()
# for c in userName:
#   if c not in s:
#     s.add(c)
s = set(userName)
if len(s) % 2 == 0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
