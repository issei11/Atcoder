W,H,N = map(int,input().split())
grid = [[1 for _ in range(W)] for _ in range(H)]
for _ in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        for i in range(H):
            for j in range(x):
                grid[i][j] = 0
    elif a == 2:
        for i in range(H):
            for j in range(x,W):
                grid[i][j] = 0
    elif a == 3:
        for i in range(y):
            for j in range(W):
                grid[i][j] = 0
    elif a == 4:
        for i in range(y,H):
            for j in range(W):
                grid[i][j] = 0
ans = 0
for i in range(H):
    for j in range(W):
        ans += grid[i][j]
print(ans)
#2022/8/12 00:07:28