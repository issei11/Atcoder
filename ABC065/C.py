def factorial(n,m):
    ans = 1
    for i in range(1,n+1):
        ans = (ans*i)%m
    return ans

mod = 10**9+7
N,M = map(int,input().split())
if N == M:
    print((factorial(N,mod)*factorial(M,mod)*2)%mod)
elif abs(N-M) == 1:
    print((factorial(N,mod)*factorial(M,mod))%mod)
else:
    print(0)
#2022/8/23 00:10:22