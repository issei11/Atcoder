H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))

a = []
for i in range(N):
    for j in range(A[i]):
        a.append(i+1)

c = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    if i%2 == 0:
        for j in range(W):
            c[i][j] = a[i*W+j]
    else:
        for j in range(W):
            c[i][j] = a[i*W+j]
        c[i] = c[i][::-1]

for i in range(H):
    print(*c[i])

#2022/8/25 00:10:00