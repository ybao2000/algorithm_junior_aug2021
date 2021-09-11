s = input()
s = s.lower()
k = ""
v = ["a", "e", "i", "o", "u", "y"]

for i in range(len(s)):
    if s[i] not in v:
        k += "."
        k += s[i]
print(k)