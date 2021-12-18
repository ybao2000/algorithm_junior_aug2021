while True:
  vals = [int(val) for val in input().split()]  # list comprehensino
  # vals = list(map(int, input().split()))

  n = vals[0]  # first is n
  if n == 0:
    break
  elif n == 1:
    print(0)    
  else:
    seqs = vals[1:] # this is the sequence
    diffs = []  # we only need differences
    for i in range(1, n):
      diffs.append(seqs[i]-seqs[i-1])
    # using brute force to get the shortest pattern
    for i in range(0, len(diffs)):
      # you need 2 auxiliary variables
      isPattern = True
      pattern = diffs[:i+1]
      size = i+1  # this is for convenience
      for j in range(size, len(diffs)):
        if (diffs[j] != pattern[j%size]):
          isPattern = False
          break
      if isPattern:
        print(size)
        break



