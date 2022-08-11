N,A = map(int,input().split())
x = [0] + list(map(int,input().split()))
dp = [[[0 for _ in range(A*N+1)] for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    dp[i][0][0] = 1

for i in range(1,N+1):
    for j in range(N+1):
        for k in range(A*N+1):
            if k-x[i] >= 0:
                dp[i][j][k] = dp[i-1][j-1][k-x[i]]+dp[i-1][j][k]
            else:
                dp[i][j][k] = dp[i-1][j][k]

ans = 0
for n in range(1,N+1):
    ans += dp[N][n][A*n]
print(ans)
#2022/8/11 00:36:45