def power_mod(x,n,m):
    if n == 0:
        return 1
    else:
        tmp = power_mod(x*x%m , n//2,m)
        if n%2:
            tmp = tmp*x%m
        return tmp

N = int(input())
mod = 998244353
if N%2 == 0:
    print(power_mod(2,2**N,mod)-1)
else:
    print()
