def prime_all(n):
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False
    i = 2
    while i*i <= n:
        if is_prime[i]:
            for k in range(i*i, n+1, i):
                is_prime[k] = False
        i += 1
    list = []
    for i in range(2,n+1):
        if is_prime[i]:
            list.append(i)
    return list

N = 10**5+2
x = [0 for _ in range(N)]
X = [0]
prime = set(prime_all(N))
for i in range(3,N):
    if i in prime and (i+1)//2 in prime:
        x[i] += 1

for i in range(1,N):
    X.append(X[-1]+x[i])

Q = int(input())
for _ in range(Q):
    l,r = map(int,input().split())
    print(X[r]-X[l-1])

#2022/8/30 00:08:38