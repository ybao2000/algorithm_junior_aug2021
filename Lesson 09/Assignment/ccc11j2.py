h = int(input())
M = int(input())
t = 1 # you should start time at 1 (hr)
touched = False
while t <= M:
  # A = -6 * t**4 + h * t**3 + 2 *t**2 + t
  t2 = t*t
  t3 = t2*t
  t4 = t3*t
  A = -6 * t4 + h * t3 + 2 * t2 + t
  if A <= 0:   # you found it
    print("The balloon first touches ground at hour:")
    print(t)
    touched = True
    # you need to exit the while loop
    break
  # don't forget to increase t
  t += 1
# else:
#   print("The balloon does not touch ground in the given time.")
if not touched:
  print("The balloon does not touch ground in the given time.")
