b = 124
print(b)
#  set 1 at some position
# b = b | (1<<2)
# print(b)

# set 0 at some position (clear a bit)
# b = b & (~(1<<2))
# print(b)

# togglet a bit at some position
# b = b ^ (1<<3)

# test a bit (if it's 1 then true, else false) at some position
print(bin(b), bin(1<<3))
b = b & (1<<3)
print(b)