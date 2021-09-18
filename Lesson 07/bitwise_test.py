a = 100
b = 23

# we have 3 bit operation: & (and), | (or), ^ (exclusive or)
c = a | b # & is a bit-wise operation
print(c)

print(bin(a))
print(bin(b))
print(bin(c))

print(bin(~c))  # this is complicated