def count_points(cards):
  points = 0
  if 'J' in cards:
    points += 1
  if 'Q' in cards:
    points += 2
  if 'K' in cards:
    points += 3
  if 'A' in cards:
    points += 4   
  if len(cards) == 0:
    points += 3
  elif len(cards) == 1:
    points += 2
  elif len(cards) == 2:
    points += 1
  return points

def print_format(suit, cards, points):
  txt = suit + " " + " ".join(cards)
  print(txt.ljust(29, ' '), points)

line = input()
idx_d = line.find('D')
list_c = list(line[1:idx_d])
# print(list_c)
idx_h = line.find('H')
list_d = list(line[idx_d+1: idx_h])
# print(list_d)
idx_s = line.find('S')
list_h = list(line[idx_h+1: idx_s])
# print(*list_h)
list_s = list(line[idx_s+1:])
# print(*list_s)
print("Cards Dealt              Points")
p_c = count_points(list_c)
p_d = count_points(list_d)
p_h = count_points(list_h)
p_s = count_points(list_s)
print_format("Clubs", list_c, p_c)
print_format("Diamonds", list_d, p_d)
print_format("Hearts", list_h, p_h)
print_format("Spades", list_s, p_s)
summary = f"Total {p_c+p_d+p_h+p_s}"
print(summary.rjust(31, ' '))