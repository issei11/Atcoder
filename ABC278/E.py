H,W,N,h,w = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
check = [[-1,1000,-1,-1] for _ in range(N)]

for i in range(H):
    for j in range(W):
        if check[A[i][j]][0] == -1:
            check[A[i][j]][0] = i
        if check[A[i][j]][1] > j:
            check[A[i][j]][0] = j
        if check[A[i][j]][2] < j:
            check[A[i][j]][0] = j
        if check[A[i][j]][3] < i:
            check[A[i][j]][0] = i
