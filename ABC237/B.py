H,W = map(int,input().split())
A = []
for i in range(H):
    A_W = list(map(int,input().split()))
    A.append(A_W)

B = [[0]*H for i in range(W)]
for i in range(H):
    for j in range(W):
        B[j][i] = A[i][j]

for i in range(W):
    print(*B[i])
#2022/4/26 00:06:38