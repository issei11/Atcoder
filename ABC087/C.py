N = int(input())
A = [list(map(int,input().split())) for _ in range(2)]
ans = 0
tmp = 0
for i in range(N):
    for j in range(N):
        if j <= i:
            tmp += A[0][j]
        if j >= i:
            tmp += A[1][j]
    ans = max(ans,tmp)
    tmp = 0
print(ans)
#2022/8/30 00:04:10