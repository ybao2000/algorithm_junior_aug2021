def convert(t):
  if t < 0:
    return t+2400
  elif t > 2400:
    return t-2400
  else:
    return t

t_o = int(input())
print(f"{t_o} in Ottawa")
t_v = convert(t_o - 300)
print(f"{t_v} in Victoria")
t_e = convert(t_o - 200)
print(f"{t_e} in Edmonton")
t_w = convert(t_o - 100)
print(f"{t_w} in Winnipeg")
print(f"{t_o} in Toronto")
t_h = convert(t_o + 100)
print(f"{t_h} in Halifax")
m = t_o % 100
if m < 30:
  t_s = convert(t_o + 130)
else:
  h = t_o // 100
  t_s = convert(h*100+200+m-30)
print(f"{t_s} in St. John's")
