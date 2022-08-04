N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
if len(A) != 0:
    if A[0]-1 == 0:
        B = []
    else:
        B = [A[0]-1]
    for i in range(1,M):
        if A[i]-A[i-1]-1 != 0:
            B.append(A[i]-A[i-1]-1)
    if N-A[M-1] > 0:
        B.append(N-A[M-1])
    if len(B) != 0:
        k = min(B)
    ans = 0
    for i in range(len(B)):
        if B[i]%k == 0:
            ans += B[i]//k
        else:
            ans += B[i]//k+1
    print(ans)
else:
    print(1)
#2022/6/9 00:20:48