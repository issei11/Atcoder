def gcd(a,b): #O(log min(a,b)
    return gcd(b,a%b) if b else a

a,b,c = map(int,input().split())

if c%gcd(a,b) == 0:
    print('YES')
else:
    print('NO')
#2022/8/20 00:06:09