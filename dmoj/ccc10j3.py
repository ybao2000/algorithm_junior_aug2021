v = [0, 0]

def convert(X):
  if X == 'A':
    return 0
  else:
    return 1

while True:
  vals = input().split()
  op = int(vals[0])
  if op == 7:
    break
  else:
    i = convert(vals[1])    
    if op == 1:
      v[i] = int(vals[2])
    elif op == 2:
      print(v[i])    
    elif op == 3:
      j = convert(vals[2])
      v[i] = v[i] + v[j]
    elif op == 4:
      j = convert(vals[2])
      v[i] = v[i] * v[j]    
    elif op == 5:
      j = convert(vals[2])
      v[i] = v[i] - v[j]       
    else:
      j = convert(vals[2])
      v[i] = v[i] // v[j]         