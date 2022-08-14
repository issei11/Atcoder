mod = 10**9+7
N = int(input())

d = [1 for i in range(1001)]

n = 0
for i in range(2,N+1):
    n = i
    for j in range(2,i+1):
        while n%j == 0:
            d[j] += 1
            n = n//j

ans = 1
for i in range(N+1):
    ans *= d[i]
    ans = ans%mod
print(ans)
#2022/8/14 00:14:34