quarters = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())
times =0

cur_m = 1
while quarters > 0:
  # every time you have quarters, you just play
  # every play, increase times, decrease quarters
  times += 1
  quarters -= 1
  if cur_m == 1:
    m1 += 1
    if m1 == 35:
      quarters += 30
      m1 = 0
    cur_m = 2
  elif cur_m == 2:
    m2 += 1
    if m2 == 100:
      quarters += 60
      m2 = 0
    cur_m = 3
  elif cur_m == 3:
    m3 += 1
    if m3 == 10:
      quarters += 9
      m3 = 0
    cur_m = 1

print(f"Martha plays {times} times before going broke.")
