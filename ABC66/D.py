N,K = map(int,input().split())
mod = 998244353

dp = [[0 for j in range(K+1)] for i in range(N+1)]
for i in range(1,N+1):
    dp[i][1] = 1
for j in range(1,K+1):
    dp[1][j] = 1

for i in range(2,N+1):
    S = 1
    for j in range(2,K+1):
        if i<j:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = (dp[i][j-1]+dp[i-1][j]*2-S)%mod
            S = (S+dp[i-1][j])%mod
print(dp[N][K])