def power_mod(x,n,m):
    if n == 0:
        return 1
    else:
        tmp = power_mod(x*x%m , n//2,m)
        if n%2:
            tmp = tmp*x%m
        return tmp

N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7
A.sort()
if N%2 == 0:
    check = [(i//2)*2+1 for i in range(N)]
    if A != check:
        print(0)
        exit()
else:
    check = [((i+1)//2)*2 for i in range(N)]
    if A != check:
        print(0)
        exit()

print(power_mod(2,N//2,mod))
#2022/8/12 00:12:56