N,M = map(int,input().split())
A = list(map(int,input().split()))

accum = [0]
for i in range(N):
    accum.append(accum[-1]+A[i])
ans = 0
for i in range(M):
    ans += (i+1)*A[i]
tmp = ans
for i in range(1,N-M+1):
    tmp = tmp-(accum[i+M-1]-accum[i-1])+M*A[i+M-1]
    ans = max(ans,tmp)
print(ans)