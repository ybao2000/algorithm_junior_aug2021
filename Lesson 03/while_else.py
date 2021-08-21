num = int(input())  # read in a number

while num >= 0:
  if num == 2:
    break  
  print(num)
  num -= 1  # decrease
else:
  print("The number is less than 0")

print("Done")
