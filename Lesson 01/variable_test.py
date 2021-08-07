import math

i = 1             # int
s1 = "app'le"      # string
s2 = 'pe"ar'       # string
s3 = '''ban
ana''' # string, allow multiple line
s4 = """ora
nge""" # string
pi = 3.14         # float

# what if I need both: 5'17"
# escape!!! 
# \n: next line, \t: tab, \": double quote symbol, \': single quote symbol, unicode
height = "5'7\""
# boolean
b1 = True
b2 = False
z = None  # None mean nothing, not assigned

b3 = b1 and b2  # expression
s = s1 + " " + height
r = 5
perimeter = 2 * r * math.pi
print(s)
print(perimeter)

a = 10120202022012020202020 # super big number
b = 20202020202022020202020
c = a + b
print(c)