# print('*' * 100)
# print("Hello"*10)
f = ["apple", "banana", "cherry", "date", "egg"]
g = [1, 2, 3, 4, 5]

# what if I want them ***apple***, *banana*, 
for i in range(5):
  # print(item.center(10, "-"))
  print(f[i].rjust(10), g[i], sep=' ')