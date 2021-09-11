kbs = """qwertyuiop
asdfghjkl;
zxcvbnm,./"""

mode = input()
letters = input()

for letter in letters:
  index = kbs.find(letter)
  if mode == 'R':
    new_letter = kbs[index-1]
  else:
    new_letter = kbs[index+1]
  print(new_letter, end='') # end='' means no new line
print()   # print a new line
