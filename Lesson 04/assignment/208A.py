# words = input()
# print(words.replace("WUB", ' ').lstrip().rstrip())

# print(" ".join(input().replace("WUB", " ").lstrip().rstrip().split()))


words = input()
v = [w for w in words.split("WUB") if w != '']
print(" ".join(v))