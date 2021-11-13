# define a set of vowels
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

while True:
  word = input()
  if word == "quit!":
    break
  
  lw = len(word)
  # three condictions:
  # length more than 4
  # end with "or"
  # the last third one cannot be vowel
  if lw > 4 and word.endswith("or") and word[-3] not in vowels:
    # we want everything the same except replace the last two with our
    # word.replace("or", "our")
    print(word[:lw-2]+'our')
  else:
    print(word)