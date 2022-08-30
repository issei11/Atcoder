N = int(input())
F = [list(map(int,input().split())) for _ in range(N)]
P = [list(map(int,input().split())) for _ in range(N)]

ans = -float('inf')
tmp = 0
c = [0 for _ in range(N)]
for i in range(1,2**10):
    for j in range(10):
        if (i>>j)&1:
            for k in range(N):
                c[k] += F[k][j]
    for j in range(N):
        tmp += P[j][c[j]]
    ans = max(ans,tmp)
    tmp = 0
    c = [0 for _ in range(N)]
print(ans)
#2022/8/30 00:14:24