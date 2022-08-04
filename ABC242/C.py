
m = 998244353

def pow(x,n):
    m = 998244353
    if n == 0:
        return 1
    tmp = pow(x*x % m, n//2)
    if n%2:
        tmp = tmp*x % m
    return tmp

n = int(input())
print(20*pow(3,n-2)+3*pow(2,n-1)-1)

#2022/4/21 01:30:30 バグ取れず
#追記：一般項にミスあり。普通に無理ゲーだった。