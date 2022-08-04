def gcd(a,b):
    return gcd(b,a%b) if b else a

A,B,C = map(int,input().split())

g = gcd(A,gcd(B,C))
print(A//g+B//g+C//g-3)