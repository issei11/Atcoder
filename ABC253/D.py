def gcd(a,b): #O(log min(a,b)
    return gcd(b,a%b) if b else a

def lcm(A,B):
    return A*B//gcd(A,B)

N,A,B = map(int,input().split())
s2 = N*(N+1)
s2_a = A*(N//A)*((N//A)+1)
s2_b = B*(N//B)*((N//B)+1)
g = lcm(A,B)
s2_g = g*(N//g)*((N//g)+1)
ans = (s2-s2_a-s2_b+s2_g)//2
print(ans)