def gcd(a,b): #O(log min(a,b))
    return gcd(b,a%b) if b else a

N = int(input())
A = list(map(int,input().split()))
X = min(A)
for i in range(N):
    A[i] -= X
g = gcd(A[0],A[1])
for i in range(2,N):
    g = gcd(g,A[i])
if g == 1:
    print(2)
else:
    print(1)