s = "Funny Cat Garfield Dressed As Easter Bunny"

# I want "FCGDAEB"
# list_s = s.split()
# print(list_s)
# list_b = [word[0] for word in list_s]
# print(list_b)
# print(str.join('-', list_b))

print(str.join('', [word[0] for word in s.split()]))
