N,L = map(int,input().split())
mod = 10**9+7
dp = [1 for _ in range(N+1)]
for i in range(1,N+1):
    if i >= L:
        dp[i] = (dp[i-1]+dp[i-L])%mod
    else:
        dp[i] = dp[i-1]
print(dp[N]%mod)
#2022/8/24 00:06:54