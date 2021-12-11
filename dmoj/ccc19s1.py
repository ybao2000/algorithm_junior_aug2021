n1, n2, n3, n4 = 1, 2, 3, 4

vals = input()
for val in vals:
  if val == 'H': # horizontal flip
    n1, n2, n3, n4 = n3, n4, n1, n2
  else:
    n1, n2, n3, n4 = n2, n1, n4, n3

print(f"{n1} {n2}")
print(f"{n3} {n4}")
  