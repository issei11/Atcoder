N,Q = map(int,input().split())
A = list(map(int,input().split()))
start = 0
for _ in range(Q):
    t,x,y = map(int,input().split())
    x -= 1
    y -= 1
    if t == 1:
        A[x-start],A[y-start] = A[y-start],A[x-start]
    elif t == 2:
        start += 1
        start = start%N
    elif t == 3:
        print(A[x-start])
