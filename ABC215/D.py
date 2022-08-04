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
    return list,is_prime

N,M = map(int,input().split())
A = list(map(int,input().split()))

ans = [True]*(M+1)
ans[0] = False
p_list,p_check = prime_all(M)
i = 0
for a in A:
    while p_list[i] <= a and i < len(p_list):
        if a%p_list[i] == 0:
            for k in range(p_list[i], M+1, p_list[i]):
                ans[k] = False
        i += 1
    i = 0
print(sum(ans))
for x in range(M+1):
    if ans[x]:
        print(x)