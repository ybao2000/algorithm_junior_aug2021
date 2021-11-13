Y = int(input())
while True:
  Y += 1
  sY = str(Y) # convert the number into str
  # keep in mind string is a special tuple, which is also iterable
  ss = set(sY)  # convert the string into set
  if len(sY) == len(ss):
    print(Y)
    break
