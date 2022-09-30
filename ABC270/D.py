import bisect
N,K = map(int,input().split())
A = list(map(int,input().split()))

t = 0
a = 0

cnt = 0
while N >= A[0]:
    idx = bisect.bisect(A,N)-1
    if cnt%2 == 0:
        t += A[idx]
        N -= A[idx]
    else:
        a += A[idx]
        N -= A[idx]
    cnt += 1
print(t)