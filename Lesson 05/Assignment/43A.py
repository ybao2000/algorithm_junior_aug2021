n = int(input())
repo = {}
for _ in range(n):  # if you don't need the index, then you can use _
  name = input()
  if name in repo:
    repo[name] += 1 # increase the number if already exists
  else:
    repo[name] = 1  # this is the first time, so set value as 1

max_score = 0 # initial max score, make sure all scores > this number
for item in repo.items(): # items() is going to give you both key, value
  if item[1] > max_score:   #[1] means value, [0] means key
    name = item[0]
    max_score = item[1]
  
print(name)