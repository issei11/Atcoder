N,K = map(int,input().split())
A = list(map(int,input().split()))
As = sorted(A)

tmp = []
for i in range(K):
    for j in range(i,N,K):
        tmp.append(A[j])
    tmp.sort()
    for j in range(len(tmp)):
        A[j*K+i] = tmp[j]
    tmp = []

As = sorted(A)
print("Yes" if As == A else "No")