vals = input().split(':')
h = int(vals[0])
m = int(vals[1])
for i in range(120):  # this is 2 hours
  if 7<=h<10 or 15<=h<19: # this is rush hour
    m += 2  # double the increase
  else:
    m += 1  # normal time increase
  if m >= 60:
    h += 1
    m = m % 60
  if h == 24:
    h = 0
if h < 10:
  str_h = '0' + str(h)
else:
  str_h = str(h)
if m < 10:
  str_m = '0' + str(m)
else:
  str_m = str(m)
print(str_h + ':' + str_m)