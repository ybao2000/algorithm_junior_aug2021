num = int(input())  

# while num >= 0:
#   if num % 2 == 0:  # skip all even numbers
#     num -= 1
#     continue
#   print(num)
#   num -= 1

while num >= 0:
  if num % 2 == 1:
    print(num)
  num -= 1
print("Done")
