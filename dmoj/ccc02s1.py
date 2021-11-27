pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
total = int(input())
tc = 0
mc = total
for i in range(total//pink+1):
  for j in range(total//green+1):
    for k in range(total//red+1):
      remain = total -  (i * pink + j * green + k * red)
      if remain >=  0 and remain % orange == 0:
        l = remain // orange
        print(f"# of PINK is {i} # of GREEN is {j} # of RED is {k} # of ORANGE is {l}")
        tc += 1
        mc = min(mc, i+j+k+l)

print(f"Total combinations is {tc}.")
print(f"Minimum number of tickets to print is {mc}.")