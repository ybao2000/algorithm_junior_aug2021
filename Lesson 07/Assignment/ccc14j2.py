V = input()
line = input()
na = line.count("A")
nb = line.count("B")

if na > nb:
  print("A")
elif nb > na:
  print("B")
else:
  print("Tie")