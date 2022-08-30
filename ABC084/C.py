N = int(input())
C = []
S = []
F = []
for _ in range(N-1):
    c,s,f = map(int,input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(N-1):
    x = S[i]+C[i]
    for j in range(i+1,N-1):
        if x <= S[j]:
            x = S[j]+C[j]
        else:
            x = ((x-S[j]+F[j]-1)//F[j])*F[j]+S[j]+C[j]
    print(x)
print(0)

#2022/8/30 00:19:05