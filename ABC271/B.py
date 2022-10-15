N,Q = map(int,input().split())
accum_L = [0]
A = []
for _ in range(N):
    a = list(map(int,input().split()))
    L = a[0]
    accum_L.append(L+accum_L[-1])
    for i in range(1,len(a)):
        A.append(a[i])

for _ in range(Q):
    s,t = map(int,input().split())
    print(A[accum_L[s-1]+t-1])