line = input()
# you need a set to store all distinct numbers
letters = set() # empty set
for ch in line:
  # loop through all chars
  if ch != '{' and ch != '}' and ch != ',' and ch != ' ':
    letters.add(ch)
print(len(letters))
