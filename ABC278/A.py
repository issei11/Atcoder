N,K = map(int,input().split())
A = list(map(int,input().split()))

ans = []
if N <= K:
    for i in range(N):
        ans.append(0)
    print(*ans)
else:
    for i in range(K):
        ans.append(0)
    for i in range(N-K):
        ans.append(A[-(i+1)])
    ans.reverse()
    print(*ans)
