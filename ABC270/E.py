N,K = map(int,input().split())
A = list(map(int,input().split()))

B = K//N
C = K%N

for i in range(N):
    A[i] -= B
    if i < C:
        A[i] -= 1

D = 0
for i in range(N):
    if A[i] < 0:
        D += abs(A[i])
        A[i] = 0


