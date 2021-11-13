from collections import Counter

s = "Hello world"

# Counter returns an object similar to dictionary
# the key is the characters
# the value is the occurrence

d = Counter(s)
print(d)

# check the occurrence of some character
print(d['l'])
print(d['x'])

# you can update
t = "Twinkle Twinkle Little Star"
d.update(t) # do the merge
print(d)

# you can check the most common letter
print(d.most_common())

# you can use Counter similar to dictionary
# for key  in d.keys():
#   print(key)

# for value in d.values():
#   print(value)

# for item in d.items():
#   print(item)

for elem in d.elements():
  print(elem)