# one is using range()
total = 0
for i in range(1, 101, 2):    # start: 1, end: 101 (excluded), inc: 2 (by default, 1)
  total += i
print(total)

nums = [1, 3, 5, 7, 9, 10]    # you can use for loop for list

total2 = 0
for num in nums:
  if num % 2 == 0:  #  only calucate the even numbers
    total2 += num * num
print(total2)
