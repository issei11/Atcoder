H, W = map(int,input().split())
C = []
for i in range(H):
    C_i = input()
    C.append(C_i)
dp = [[False]*(W+1) for i in range(H+1)]
dp[0][1] = dp[1][0] =True

ans = 1
tmp = 0

for i in range(1,H+1):
    for j in range(1,W+1):
        if C[i-1][j-1] == '.':
            dp[i][j] = dp[i-1][j] or dp[i][j-1]
            if dp[i][j]:
                tmp = i+j-1
                ans = max([ans,tmp])

print(ans)
#2022/5/1 00:27:34