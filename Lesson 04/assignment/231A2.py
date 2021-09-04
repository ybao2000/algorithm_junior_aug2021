c = 0
for i in range(int(input())):
	a = map(int, input().split(" "))
	if sum(a) >= 2:
		c += 1

print(c)

# c = 0
# for i in range(int(input())):
# 	a = [int(val) for val in input().split()]
# 	if sum(a) >= 2:
# 		c += 1

# print(c)