from collections import Counter


a = int(input())
b = ""
teams = []
for i in range(a):
    c = input()
    teams.append(c)
counts = Counter(teams)
print(sorted(teams, key=lambda x: -counts[x])[0])