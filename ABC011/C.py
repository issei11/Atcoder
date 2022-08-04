N = int(input())
NG = [int(input()) for _ in range(3)]
dp = [0 for _ in range(300+1)]
dp[0] = 0
for i in range(3):
    dp[NG[i]] = 101
for i in range(1,300+1):
    if dp[i] == 0:
        if i >= 3:
            dp[i] = min(dp[i-1],dp[i-2],dp[i-3])+1
        elif i == 2:
            dp[i] = min(dp[i-1],dp[i-2])+1
        else:
            dp[i] = dp[i-1]+1
print('YES' if dp[N] <= 100 else 'NO')
#2022/8/1 00:32:53 1WA