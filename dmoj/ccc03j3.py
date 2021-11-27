paths = {9: 34, 40: 64, 67: 86, 54: 19, 90: 48, 99: 77} # using dictionary
position = 1

while True:
  step = int(input())
  if step == 0:
    print("You Quit!")
    break
  else:
    next_position = position + step
    if next_position == 100:
      print("You are now on square 100")
      print("You Win!")
      break
    elif next_position < 100:
      if next_position in paths:
        next_position = paths[next_position]
      position = next_position
    print(f"You are now on square {position}")