sites = ['HOME']
dirs = []
while True:
  dir = input()
  if dir == 'L':
    dirs.append('RIGHT')
  else:
    dirs.append('LEFT')    
  site = input()
  if site == 'SCHOOL':
    break
  else:
    sites.append(site)
for i in range(len(sites)-1, -1, -1):
  dir = dirs[i]
  site = sites[i]
  if site == 'HOME':
    print(f"Turn {dir} into your HOME.")
  else:
    print(f"Turn {dir} onto {site} street.")

