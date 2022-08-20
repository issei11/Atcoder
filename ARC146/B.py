N,M,K = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
A = []
for a in x:
    A.append(bin(a)[2:].zfill(30))
    print(A[-1])

c = []
cnt = 0
for d in range(30):
    for i in range(N):
        if A[i][d] == 1:
            cnt += 1
    if (K-cnt)*2**(29-d) <= M:
        M = M-(K-cnt)*2**(29-d)