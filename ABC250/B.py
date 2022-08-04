N,A,B = map(int,input().split())

ans = [['.']*(N*B) for i in range(N*A)]
for i in range(N*A):
    for j in range(N*B):
        if (i%(2*A)>= A and j%(2*B)<B) or (i%(2*A) < A and j%(2*B)>=B):
            ans[i][j] = '#'
for i in range(N*A):
    print(''.join(ans[i]))