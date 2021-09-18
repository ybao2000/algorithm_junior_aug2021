def cast_spell(num):
  new_num = 0
  while num > 0:
    new_num += num % 10 # add the last digit
    num = num // 10     # get rid of the last digit
  return new_num

a = input()
i_count = 0
if len(a) > 1:
  # need to cast spell to string
  num = 0
  for ch in a:
    num += int(ch)   # add up the digit
  i_count += 1  # you just made one spell
  while num >= 10:
    num = cast_spell(num)
    i_count += 1    # every time you make the spell, increase the cout
print(i_count)
