a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

def calc_steps(f, b, s):
  # f is forward, b is backward, s is the absolute steps
  n = s // (f+b)  # q is the # of the cycles
  r = s % (f+b)   # r is the remaining steps
  total = n * (f-b)
  if r <= a:
    total += r
  else:
    total += 2 * f - r
  return total

s1 = calc_steps(a, b, s)
s2 = calc_steps(c, d, s)
if s1 > s2:
  print("Nikky")
elif s1 < s2:
  print("Byron")
else:
  print("Tied")
