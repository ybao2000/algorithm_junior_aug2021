a, b, c, d, e = "A", "B", "C", "D", "E"
while True:   # infinite loop, you need break!!!
  bt = int(input())
  n = int(input())

  if bt == 4:
    # if button is 4, means its done
    break
  
  for _ in range(n):  # you need repeat n times
    if bt == 1:
      a, b, c, d, e = b, c, d, e, a
    elif bt == 2:
      a, b, c, d, e = e, a, b, c, d
    elif bt == 3:
      a, b = b, a

print(a, b, c, d, e)