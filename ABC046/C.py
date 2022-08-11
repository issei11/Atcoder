def gcd(a,b): #O(log min(a,b))
    return gcd(b,a%b) if b else a

N = int(input())
T,A = map(int,input().split())
t = T
a = A
for _ in range(N-1):
    T,A = map(int,input().split())
    l = T*A//gcd(T,A)
    x = (((max(T*a,A*t)+l-1)//l)*l)
    a = x//T
    t = x//A
print(a+t)
#2022/8/11 00:13:14