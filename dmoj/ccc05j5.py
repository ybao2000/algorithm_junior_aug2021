def is_monkey_word(word):
  pass

while True:
  word = input()
  if word == 'X':
    break
  if is_monkey_word(word):
    print("YES")
  else:
    print("NO")
    