def gcd(a,b): #O(log min(a,b)
    return gcd(b,a%b) if b else a

def lcm(a,b):
    return a*b//gcd(a,b)

N = int(input())
T = int(input())
l = lcm(T,1)
for i in range(1,N):
    T = int(input())
    l = lcm(l,T)
print(l)

#2022/8/25 00:06:46 1RE