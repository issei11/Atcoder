from collections import deque
inf = float('inf')
H,W = map(int,input().split())
s = [input() for _ in range(H)]

wall_num = 0
grid = [[inf for _ in range(W+2)] for _ in range(H+2)]
for i in range(H+2):
    for j in range(W+2):
        if i == 0 or i == H+1 or j == 0 or j == W+1:
            grid[i][j] = -1
        elif s[i-1][j-1] == '#':
            grid[i][j] = -1
            wall_num += 1

dx = [-1,0,0,1]
dy = [0,1,-1,0]
sx = 1
sy = 1
grid[sy][sx] = 1
gx = W
gy = H
waiting = deque()
waiting.append((sy,sx))
done = [[False for _ in range(W+2)] for _ in range(H+2)]
while len(waiting):
    now = waiting.popleft()
    ny = now[0]
    nx = now[1]
    for i in range(4):
        print(ny,nx,i,grid[ny][nx],done[ny][nx],done[ny+dy[i]][nx+dx[i]])
        if grid[ny+dy[i]][nx+dx[i]] != -1 and done[ny+dy[i]][nx+dx[i]] == False:
            grid[ny+dy[i]][nx+dx[i]] = grid[ny][nx]+1
            waiting.append((ny+dy[i],nx+dx[i]))
            print('->',ny+dy[i],nx+dx[i],done[ny+dy[i]][nx+dx[i]])
            print('len=',len(waiting))
    done[ny][nx] = True

print(H*W-wall_num-grid[gy][gx] if grid[gy][gx] != inf else -1)

#2022/8/31 00:01:07 1RE