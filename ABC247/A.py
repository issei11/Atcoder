"""
S = list(input())

S[3] = S[2]
S[2] = S[1]
S[1] = S[0]
S[0] = '0'

Sout = str(S)

for s in S:
    print(s, end ="")

print("")
"""
#2022/4/19 00:15:36

S = input()
print(f"0{S[:3]}")