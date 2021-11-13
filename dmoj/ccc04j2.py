# 4, 2, 3, 5 
# lcm is 60
a = int(input())
b = int(input())
for year in range(a, b+1, 60): # start from a, increase 60 
  print(f"All positions change in year {year}")