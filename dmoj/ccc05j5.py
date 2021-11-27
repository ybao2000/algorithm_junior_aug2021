def is_monkey_word(word):
  if is_a_word(word):
    return True
  for i in range(len(word)): # you need to check all patterns like: w1 + N + w2
    if word[i] == 'N':
      if is_a_word(word[:i]) and is_monkey_word(word[i+1:]):
        return True
  return False
  
def is_a_word(word):
  if word == 'A':
    return True
  if len(word) >= 3 and word[0] == 'B' and word[-1] == 'S' and is_monkey_word(word[1:-1]):
    return True
  return False

while True:
  word = input()
  if word == 'X':
    break
  if is_monkey_word(word):
    print("YES")
  else:
    print("NO")
    