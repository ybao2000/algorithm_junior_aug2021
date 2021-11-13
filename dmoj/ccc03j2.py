# you need infinite loop
while True:
  C = int(input())
  if C == 0:
    break
  
  a = 1
  b = C
  # find the factor pair a and b which is the closest
  k = 2
  while k * k <= C:
    if C % k == 0:  # you find a better one
      a = k
      b = C//k
    # don't forget to increase k
    k += 1  
  p = 2 * (a + b)
  print(f"Minimum perimeter is {p} with dimensions {a} x {b}")