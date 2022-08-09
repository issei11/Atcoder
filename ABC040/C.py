N = int(input())
a = list(map(int,input().split()))
dp = [0 for _ in range(N)]
dp[1] = abs(a[0]-a[1])
for i in range(2,N):
    dp[i] = min(dp[i-1]+abs(a[i]-a[i-1]),dp[i-2]+abs(a[i]-a[i-2]))
print(dp[N-1])
#2022/8/9 00:03:52