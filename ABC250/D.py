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

N = int(input())

p = prime_all(int((N//2)**(1/3)+1))
p_3 = [i**3 for i in p]
cnt = 0
for i in range(len(p)-1):
    for j in range(i+1,len(p)):
        if p[i]*p_3[j] <= N:
            cnt += 1
print(cnt)