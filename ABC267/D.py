inf = float('inf')
N,M = map(int,input().split())
A = list(map(int,input().split()))

dp = [[-inf for _ in range(N+1)] for _ in range(N)]
dp[0][1] = A[0]
for i in range(N):
    dp[i][0] = 0

for i in range(1,N):
    for j in range(1,i+2):
        dp[i][j] = max(dp[i-1][j-1]+j*A[i],dp[i-1][j])
print(dp[N-1][M])