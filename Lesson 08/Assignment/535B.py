n = input()

def count_lucky_num(s):
  # base case: len = 1
  l = len(s)
  if l == 1:
    if s == '4': 
      return 1
    else:
      return 2
  t1 = count_lucky_num(s[:l-1])
  t2 = count_lucky_num(s[-1])
  return  t1 * 2+ t2

print(count_lucky_num(n))