H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H)]

ans = 0
for i in range(H-1):
    for j in range(W-1):
        c = A[i][j]-B[i][j]
        ans += abs(c)
        A[i][j] -= c
        A[i+1][j] -= c
        A[i][j+1] -= c
        A[i+1][j+1] -= c

for i in range(H):
    if A[i][W-1] != B[i][W-1]:
        print('No')
        exit()
for j in range(W):
    if A[H-1][j] != B[H-1][j]:
        print('No')
        exit()

print('Yes')
print(ans)

#2022/9/19 00:08:38