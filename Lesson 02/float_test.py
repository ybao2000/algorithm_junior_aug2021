# i = 10000000000000000000000000
# # this means, i is integer, integer is accurate! the only problem for integer is overflow
# # but in Python, you don't worrry about overflow, because python already handled it for you!
# # The beauty of Python is you don't have overflow problem for integer
# # python can deal with big number
# print(i+1)

a = 0.1
b = 0.1 * 10
c = a + a + a + a + a + a + a + a + a + a
print(a, b, c)
# float is not accurate!!!! How accurate is depending on how you store the variable
# integer, 4-bytes, 32 bits to store it
# float, it is stored in 2 parts, one is called precision, another one is exponent
# a = 12344566669.322020202020
# actually, it is store as 1.234456666...... as precision, and 10 as exponent
# a = 1.23446.... 10^10
a = 1e9+7
b = int(a)
print(a, b)