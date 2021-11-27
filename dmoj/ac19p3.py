expr = input().replace('(', '').replace('+', '').replace(')', '').split()
# print(expr)
s = sum(int(v) for v in expr)
print(s)