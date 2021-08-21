x = int(input())
# Wooooooooow
# way 1: this is using concatenate of strings
# you using multiplication of string
# print('W' + 'o'*x + 'w')

# way 2: this is using f-string
# ox = 'o'*x
# print(f'W{ox}w')

# way 3: iterative, and using end='' to prevent going to the next line
print('W', end='')  # end='' means don't go to next line
for _ in range(x):
  print('o', end='')  # don't go to next line
print('w')    # this will go to the next line
