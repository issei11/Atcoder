mod = 10**9+7

N = int(input())
ans = 1
for i in range(1,N+1):
    ans *= i
    ans %= mod
print(ans)
#2022/8/17 00:01:30