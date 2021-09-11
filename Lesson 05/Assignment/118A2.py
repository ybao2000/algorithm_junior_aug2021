s = input()
s = s.lower()
repo = [] # empty list
v = ["a", "e", "i", "o", "u", "y"]

for i in range(len(s)):
    if s[i] not in v:
        repo.append('.')
        repo.append(s[i])
        # k += "."
        # k += s[i]
print(*repo, sep='')