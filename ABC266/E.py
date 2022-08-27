import math

def f(n):
    if n == 1:
        return 3.5
    i = 4
    while True:
        if i > f(n-1):
            break
        i += 1
    if i == 4:
        return 5/2+f(n-1)*(1/2)
    if i == 5:
        return 11/6+f(n-1)*(2/3)
    if i == 6:
        return 1+f(n-1)*(5/6)

N = int(input())

dp = [0 for _ in range(N)]
dp[0] = 3.5

for i in range(1,N):
    x = math.ceil(dp[i-1])
    if x == 4:
        dp[i] = 5/2+dp[i-1]*(1/2)
    if x == 5:
        dp[i] = 11/6+dp[i-1]*(2/3)
    if x == 6:
        dp[i] = 1+dp[i-1]*(5/6)

print(dp[N-1])