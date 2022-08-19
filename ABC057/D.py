N,A,B = map(int,input().split())
v = list(map(int,input().split()))

dp = [[[0,0] for _ in range(N+1)] for _ in range(N)]
dp[0][1][0] = v[0]
dp[0][1][1] = 1
for i in range(1,N):
    for j in range(1,i+2):
        if dp[i-1][j-1][0]+v[i] < dp[i-1][j][0]:
            dp[i][j][0] = dp[i-1][j][0]
            dp[i][j][1] = max(dp[i-1][j][1],1)
        elif dp[i-1][j-1][0]+v[i] > dp[i-1][j][0]:
            dp[i][j][0] = dp[i-1][j-1][0]+v[i]
            dp[i][j][1] = max(dp[i-1][j-1][1],1)
        else:
            dp[i][j][0] = dp[i-1][j-1][0]+v[i]
            dp[i][j][1] = max(dp[i-1][j-1][1],1)+max(dp[i-1][j][1],1)

ans_max = [dp[N-1][A][0],A]
ans_num = dp[N-1][A][1]
for j in range(A+1,B+1):
    if ans_max[0]*j < ans_max[1]*dp[N-1][j][0]:
        ans_max = [dp[N-1][j][0],j]
        ans_num = dp[N-1][j][1]
    elif ans_max[0]*j ==  ans_max[1]*dp[N-1][j][0]:
        ans_num += dp[N-1][j][1]
print(ans_max[0]/ans_max[1])
print(ans_num)
#2022/8/17 00:39:46