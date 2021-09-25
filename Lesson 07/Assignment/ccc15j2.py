line = input()
h = line.count(":-)")
s = line.count(":-(")
if h>s:
  print("happy")
elif h<s:
  print("sad")
elif s == 0:
  print("none")
else:
  print("unsure")