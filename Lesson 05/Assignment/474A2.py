kbs = """qwertyuiop 
  asdfghjkl;
  zxcvbnm,./"""

# convert the above string into a dictionary!
repo = {}   #empty dictionary
# anybody knows how to define an empty set instead of empty dictionary
# set2 = set()
for index, letter in enumerate(kbs):
  repo[letter] = index  # use letter as key

# print(repo)
mode = input()
letters = input()

for letter in letters:
  index = repo[letter]
  if mode == 'R':
    new_letter = kbs[index-1]
  else:
    new_letter = kbs[index+1]
  print(new_letter, end='') # end='' means no new line
print()   # print a new line
