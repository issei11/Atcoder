N = int(input())
L = [0 for _ in range(N+1)]

L[0] = 2
L[1] = 1
for i in range(2,N+1):
    L[i] = L[i-1]+L[i-2]
print(L[N])

#2022/8/29 00:02:16