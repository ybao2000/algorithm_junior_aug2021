books = input()
L = books.count("L")
M = books.count("M")
S = books.count("S")

L_section = books[:L] # these are the books currently in L section
M_section = books[L:L+M]  # these are the books currently in M section
S_section = books[L+M:] #these are the books currently in S section

L_M = L_section.count("M")  # this the mis-pos of M book in L section
L_S = L_section.count("S")  # mis-pos of S book in L section
M_L = M_section.count("L")
M_S = M_section.count("S")  
S_L = S_section.count("L")
S_M = S_section.count("M")

# direct swap
# first check L_M and M_L
swap_L_M = min(L_M, M_L)
L_M -= swap_L_M
M_L -= swap_L_M
swap_L_S = min(L_S, S_L)
L_S -= swap_L_S
S_L -= swap_L_S
swap_M_S = min(M_S, S_M)
M_S -= swap_M_S
S_M -= swap_M_S

# rotation
rotation_MSL = 2 * L_M 
rotation_SLM = 2 * L_S
print(swap_L_M + swap_L_S + swap_M_S + rotation_MSL + rotation_SLM)
