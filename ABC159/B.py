S = input()
N = len(S)
S_mae = S[:(N-1)//2]
S_ushiro = S[(N+1)//2:]
print("Yes" if S == S[::-1] and S_mae == S_mae[::-1] and S_ushiro == S_ushiro[::-1] else "No")
#2022/6/5 00:04:55