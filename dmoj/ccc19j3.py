N = int(input())
for _ in range(N):
  line = input()
  items = []
  prev_c = None
  count = 0
  for cur_c in line:
    if prev_c is None:  # this is the first char
      prev_c = cur_c
      count = 1
    elif cur_c == prev_c:
      count += 1
    else:
      # your prev_c is done
      items.append(count)
      items.append(prev_c)
      prev_c = cur_c
      count = 1
  # once the iteration is done, you still have prev_c and count
  items.append(count)
  items.append(prev_c)
  print(*items) # this is to print all items in the list, 