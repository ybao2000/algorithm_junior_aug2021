from collections import defaultdict

d = defaultdict(int)  # tell it the type of the value
d['c']  = 3
d['a'] = 1
d['b']  = 2
d['f']  = 4

d.pop('a')
d['a']  = 5
print(d)

d['x'] += 1
print(d['x'])