import math
N,X = map(int,input().split())
x = list(map(int,input().split()))

if N > 1:
    g = abs(X-x[0])
    for i in range(1,N):
        g = math.gcd(abs(x[i-1]-x[i]),g)
else:
    g = abs(X-x[0])
print(g)
#2022/6/15 00:10:16