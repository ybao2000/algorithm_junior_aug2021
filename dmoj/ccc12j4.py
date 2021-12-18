K = int(input())
letters = input()
for idx, letter in enumerate(letters):
  S = (idx+1)*3+K
  # ord() - get the ordinal number (ascii code)
  # chr() - get the letter from the ordinal number (ascii code)
  x = ord(letter) - S
  # x cannot be less than ord('A')
  if x < ord('A'):
    x += 26
  print(chr(x), end='') # print the char one by one
print() # this is to go to the next line
