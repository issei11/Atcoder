N,W = map(int,input().split())
w = []
v = []
a,b = map(int,input().split())
w.append(a)
v.append(b)
for _ in range(1,N):
    a,b = map(int,input().split())
    w.append(a-w[0])
    v.append(b)
w1 = w[0]
w[0] = 0

dp = [[[-float('inf') for k in range(3*N+1)] for j in range(N+1)] for i in range(N)]

for i in range(N):
    dp[i][0][0] = 0
if w1 <= W:
    dp[0][1][0] = v[0]

for i in range(1,N):
    for j in range(1,N+1):
        for k in range(3*N+1):
            if w1*j+k <= W and k-w[i] >= 0:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i-1][j-1][k-w[i]]+v[i])
            elif w1*j+k <= W:
                dp[i][j][k] = dp[i-1][j][k]
ans = 0
for j in range(N+1):
    ans =max(max(dp[N-1][j]),ans)
print(ans)
#2022/8/20 00:29:42