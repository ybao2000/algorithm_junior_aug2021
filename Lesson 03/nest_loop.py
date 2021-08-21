# print a right triangle 
# ****
#  ***
#   **
#    *
n = int(input())
for row in range(n):
  print(' '* row +'*'*(n-row))