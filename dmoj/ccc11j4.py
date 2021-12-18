# you use a set of locations, location is a tuple
visited = {(0, -1), (0, -2), (0, -3),
(1, -3), (2, -3), (3, -3),
(3, -4), (3, -5),
(4, -5), (5, -5),
(5, -4), (5, -3),
(6, -3), (7, -3),
(7, -4), (7, -5), (7, -6), (7, -7),
(6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7), (0, -7), (-1, -7),
(-1, -6), (-1, -5)
}
loc = (-1, -5) # this is your current location
while True: 
  vals = input().split()
  dir = vals[0]
  num = int(vals[1])
  if dir == 'q':
    break
  else:
    x, y = loc[0], loc[1]
    isSafe = True
    for step in range(1, num+1):
      if dir == 'l':
        x -= 1
      elif dir == 'r':
        x += 1
      elif dir == 'd':
        y -= 1
      else:
        y += 1
      if (x, y) in visited:
        isSafe = False
      else:
        visited.add((x, y))
    if not isSafe:
      print(x, y, 'DANGER')
      break
    else:
      print(x, y, 'safe')
      loc = (x, y)  # don't forget to update the loc
