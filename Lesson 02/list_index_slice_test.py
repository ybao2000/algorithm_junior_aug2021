list_a = [1, 2, 3, 4, 5, 6, 7, 8]

# index is a sequential number start at 0, everytime increase by 1
# you use index to get the element
print(list_a[5])

# what is I want sub-list
# this is get a sub starting from some index
list_b = list_a[2:]
print(list_b)

# what if I want the first 2
list_c = list_a[:2]
print(list_c)

# sometimes from 2 to 5
list_d = list_a[2:5]
print(list_d)

# actually, you can give increment (by default, increment is 1)
list_e = list_a[2:5:2]
print(list_e)