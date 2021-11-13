direction = ''
while True:   # infinite loop
  val = input()
  if val == '99999':
    break
  first = int(val[0])
  second = int(val[1])
  steps = val[2:5]
  if first+second > 0:
    if (first+second) % 2 == 1:
      direction = "left"
    else:
      direction = "right"
  print(f"{direction} {steps}")


