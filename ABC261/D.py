N,M = map(int,input().split())
X = list(map(int,input().split()))
bonus = [0 for i in range(N+1)]
for _ in range(M):
    c,y = map(int,input().split())
    bonus[c] = y
dp = [[0 for i in range(N+1)]for j in range(N)]
dp[0][0] = 0
dp[0][1] = X[0]+bonus[1]
for i in range(1,N):
    dp[i][0] = max(dp[i-1])
    for j in range(1,i+2):
        dp[i][j] = dp[i-1][j-1] + X[i] + bonus[j]
print(max(dp[N-1]))