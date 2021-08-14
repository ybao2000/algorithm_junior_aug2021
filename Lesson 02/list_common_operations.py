list_a = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 2]

print(sum(list_a))  # this is to give you the sum
# you can use count
print(list_a.count(2))
# what if I want to square the element?

# use list comprehension to manipulate the element
list_b = [a*a for a in list_a]
print(list_b)

# use list comprehension to filter
# I want even elements!
list_c = [a for a in list_a if a % 2 == 0]
print(list_c)

total_even = sum([a for a in list_a if a % 2 == 0])
print(total_even)

