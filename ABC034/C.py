def power_mod(x,n,m):
    if n == 0:
        return 1
    else:
        tmp = power_mod(x*x%m , n//2,m)
        if n%2:
            tmp = tmp*x%m
        return tmp

def factorial(n,m):
    ans = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2,n+1):
            ans = ans * i % m
        return ans

def combinations(n,r,m):
    return (factorial(n,m) * power_mod(factorial(n-r,m)*factorial(r,m),m-2,m))%m



W,H = map(int,input().split())
mod = 10**9+7
print(combinations(W-1+H-1,min(W-1,H-1),mod))
#2022/8/8 00:32:53