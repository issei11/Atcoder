def gcd(a,b): #O(log min(a,b)
    return gcd(b,a%b) if b else a
a,b = map(int,input().split())
l = a*b//gcd(a,b)
if l > 10**18:
    print('Large')
else:
    print(l)
#2022/8/24 00:02:11