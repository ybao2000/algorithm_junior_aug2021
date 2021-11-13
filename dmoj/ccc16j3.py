def is_palindrome(s):
  # this way is fine for simple problems
  t= s[::-1]
  return t == s
  # a better way is compare the head and tail directly
  # idx_1 = 0
  # idx_2 = len(s)-1
  # while idx_1 < idx_2:
  #   if s[idx_1] != s[idx_2]:
  #     return False
  #   idx_1 += 1
  #   idx_2 -= 2
  # return True

a = input()
longest = 1
len_a = len(a)
for i in range(len_a): # i is the start index
  for j in range(len_a-1, i, -1): # j is the end index
    b = a[i:j+1]
    len_b = len(b)
    if len_b <= longest:
      break
    if is_palindrome(b):
      longest = len_b
print(longest)