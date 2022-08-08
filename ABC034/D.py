N,K = map(int,input().split())
dp = [[[0,0] for _ in range(K+1)] for _ in range(N)]
w,p = map(int,input().split())
dp[0][1][0] = p*w
dp[0][1][1] = w
for i in range(1,N):
    w,p = map(int,input().split())
    if p*dp[i-1][1][1] > dp[i-1][1][0]:
        dp[i][1][0] = p*w
        dp[i][1][1] = w
    for j in range(2,min(i+2,K+1)):
        if j == i+1:
            dp[i][j][0] = dp[i-1][j-1][0]+p*w
            dp[i][j][1] = dp[i-1][j-1][1]+w
        elif dp[i-1][j][0]*(dp[i-1][j-1][1]+w) < dp[i-1][j][1]*(dp[i-1][j-1][0]+p*w):
            dp[i][j][0] = dp[i-1][j-1][0]+p*w
            dp[i][j][1] = dp[i-1][j-1][1]+w
        else:
            dp[i][j][0] = dp[i-1][j][0]
            dp[i][j][1] = dp[i-1][j][1]
print(dp)
print(dp[N-1][K][0]/dp[N-1][K][1])
#2022/8/8 00:55:05