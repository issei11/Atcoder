def gcd(a,b): #O(log min(a,b)
    return gcd(b,a%b) if b else a
a = int(input())
b = int(input())
n = int(input())
l = a*b//gcd(a,b)
ans = l
while ans < n:
    ans += l
print(ans)
#2022/8/8 00:04:43 1WA