"""
def power(x,n,m):
    if n == 0:
        return 1
    else:
        tmp = power(x*x%m , n//2,m)
        if n%2:
            tmp = tmp*x%m
        return tmp

m = 998244353
N = int(input())

x = 0
tmp = N
while tmp != 0:
    tmp = tmp//10
    x += 1

if x == 1:
    ans = int(N*(N+1)/2)
elif x == 2:
    ans = 45+int((N-8)*(N-9)/2)
else:
    ans = 45
    ans += (N-10**(x-1)+2)*(N-10**(x-1)+1)*power(2,m-2,m)
    for i in range(2,x):
        ans += 5*(10**i-10**(i-1)+1)*(10**(i-1)-10**(i-2))

print(ans%m)

#2022/4/26 01:07:15

"""

m = 998244353
N = int(input())

x = 0
tmp = N
while tmp != 0:
    tmp = tmp//10
    x += 1

if x == 1:
    ans = int(N*(N+1)/2)
elif x == 2:
    ans = 45+int((N-8)*(N-9)/2)
else:
    ans = 45
    ans += ((N-10**(x-1)+2)*(N-10**(x-1)+1))//2
    for i in range(2,x):
        ans += 5*(10**i-10**(i-1)+1)*(10**(i-1)-10**(i-2))

print(ans%m)

#2022/4/26 01:07:15