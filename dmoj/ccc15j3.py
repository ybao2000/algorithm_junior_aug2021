consonants = "bcdfghjklmnpqrstvwxyz" # skip the vowels a e i o u
closestVowels = "aaeeeiiiiooooouuuuuuu"
nextConsonants = "cdfghjklmnpqrstvwxyzz"

word = input()
result = []
for c in word:
  result.append(c)  # you add the char first
  idx = consonants.find(c)  # if not found, will return -1
  if idx > -1:
    result.append(closestVowels[idx])
    result.append(nextConsonants[idx])
print("".join(result))
