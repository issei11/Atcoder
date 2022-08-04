S = list(input())
N = int(input())
T = []
for _ in range(N):
    l,r = map(int,input().split())
    for i in range(len(S)):
        if l-1<=i and i<r:
            T.append(S[r+l-1-i-1])
        else:
            T.append(S[i])
    S = T
    T = []
print(*S,sep='')