N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(M):
    for j in range(N):
        if B[i] == A[j]:
            A[j] = 0
            B[i] = 0

if sum(B) == 0:
    print('Yes')
else:
    print('No')
#2022/4/22 00:05:05