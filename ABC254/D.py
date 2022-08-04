N = int(input())

A = [i for i in range(N+1)]

i = 2
while i*i < N:
    for j in range(i*i,N,i*i):
        A[j] += 2

print(sum(A))