s = input()

def calc_loc(c):
  if c == ' ':
    return (4, 2)
  elif c == '-':
    return (4, 3)
  elif c == '.':
    return (4, 4)
  else:
    seq = ord(c) - ord('A')
    return (seq//6, seq%6)

loc_1 = (0, 0)
moves = 0
for c in s:
  loc_2 = calc_loc(c)
  moves += abs(loc_1[0]-loc_2[0]) + abs(loc_1[1]-loc_2[1])
  loc_1 = loc_2
moves += abs(loc_1[0]-4) + abs(loc_1[1]-5)
print(moves)