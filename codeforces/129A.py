n = int(input())
# vals = input()  # read in the whole line
# you have to convert it into list
# list_a = vals.split()   # split is to convert the input into list
# 1   2    3   4
# print(list_a)
# list_b = []
# for a in list_a:
#   b = int(a)
#   list_b.append(b)
# print(list_b)
# you can use list comprehension!!!
# list comprehension can convert one list to another list
# list_b = [int(a) for a in list_a] 
# print(list_b)

list_a = [int(val) for val in input().split()]
count_even = 0  # initialize the counts
count_odd = 0
for a in list_a:
  if a % 2 == 0:  # a is even
    count_even += 1 # increase count_even
  else:
    count_odd += 1   # increase count_odd

if count_odd % 2 == 0:  # do you have even count of odd bags
  print(count_even)
else:
  print(count_odd)