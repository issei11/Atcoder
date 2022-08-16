N  =int(input())
grid = [list(map(int,input()))*3 for _ in range(N)]*3
ans = 0
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
tmp = 0
i2 = 0
j2 = 0
for i in range(N,2*N):
    for j in range(N,2*N):
        tmp = grid[i][j]*10**(N-1)
        i2 = i
        j2 = j
        for d in range(8):
            for k in range(N-1):
                i2 += dx[d]
                j2 += dy[d]
                tmp += grid[i2][j2]*10**(N-2-k)
            if ans < tmp:
                ans = tmp
            tmp = grid[i][j]*10**(N-1)
            i2 = i
            j2 = j
print(ans)