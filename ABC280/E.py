def power_mod(x,n,m):
    if n == 0:
        return 1
    else:
        tmp = power_mod(x*x%m , n//2,m)
        if n%2:
            tmp = tmp*x%m
        return tmp

def modInv(p,q):
    return (p*power_mod(q,m-2,m))%m

def gcd(a,b): #O(log min(a,b)
    return gcd(b,a%b) if b else a

N,P = map(int,input().split())
m = 998244353

if N == 1:
    print(1)
elif N == 2:
    g = gcd(200-P,100)
    print(modInv((200-P)//g,100//g))
else:
    Ev = [0,1,200-P]
    for i in range(3,N+1):
        tmp = (Ev[i-2]*100*P + Ev[i-1]*(100-P) + power_mod(100,i-1,m))%m
        Ev.append(tmp)
    g = gcd(Ev[N],power_mod(100,N-1,m))
    print(modInv(Ev[N]//g,power_mod(100,N-1,m)//g))