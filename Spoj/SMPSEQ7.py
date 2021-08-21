n = int(input())
S = [int(val) for val in input().split()]

def is_possible_1(S):
  dec = S[0]
  inc = None
  for val in S[1:]: # you need to start from index 1
    if val < dec:
      dec = val   # update your dec
    elif inc is None or val > inc:
      inc = val
    else:
      return False
  return True

def is_possible_2(S):
  dec = None
  inc = S[0]
  for val in S[1:]: # you need to start from index 1
    if val > inc:
      inc = val
    elif dec is None or val < dec:
      dec = val
    else:
      return False
  return True

if is_possible_1(S) or is_possible_2(S):
  print("Yes")
else:
  print("No")