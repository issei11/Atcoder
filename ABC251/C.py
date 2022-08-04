N = int(input())
rank = 0
prime_S = ''
prime_T = 0
X = set()
for i in range(N):
    S,T = input().split()
    T = int(T)
    if prime_T < T and S not in X:
        prime_S = S
        prime_T = T
        rank = i+1
    X.add(S)

print(rank)