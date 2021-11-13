m = int(input())
n = int(input())
d = {"1": "1", "8": "8", "0": "0", "9": "6", "6": "9"}

total = 0
for num in range(m, n+1):
  snum = str(num)
  idx_1 = 0
  idx_2 = len(snum)-1
  while idx_1 <= idx_2:
    if snum[idx_1] not in d or snum[idx_2] not in d:
      break
    if d[snum[idx_1]] != snum[idx_2]: 
        break
    idx_1 += 1
    idx_2 -= 1
  else:
    total += 1
print(total)
