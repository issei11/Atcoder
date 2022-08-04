import bisect
N = int(input())
A = list(map(int,input().split()))
A.sort()
Q = int(input())
score = 0
for i in range(Q):
    B = int(input())
    a = bisect.bisect_left(A,B)
    if a >= N:
        score = abs(A[a-1]-B)
    elif a>0:
        score = min(abs(A[a]-B),abs(A[a-1]-B))
    else:
        score = abs(A[a]-B)
    print(score)
