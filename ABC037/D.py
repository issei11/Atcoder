from collections import deque

inf = float('inf')
H,W = map(int,input().split())
grid = [[inf]*(H+2)]
max_map = 0
max_i = 0
max_j = 0
for i in range(1,H+1):
    a = [inf] + list(map(int,input().split())) + [inf]
    grid.append(a)
    for j in range(1,W+1):
        if max_map < a[j]:
            max_map = a[j]
            max_i = i
            max_j = j
grid.append([inf]*(H+2))

waiting = deque()
start_i = max_i
start_j = max_j
ans = [[1 for j in range(W+2)]for i in range(H+2)]
dir = [[0,1],[1,0],[-1,0],[0,-1]]
for i in range(4):
    if grid[start_i+dir[i][0]][start_j+dir[i][1]] != inf and grid[start_i+dir[i][0]][start_j+dir[i][1]] < grid[start_i][start_j]:
        ans[start_i+dir[i][0]][start_j+dir[i][1]] += ans[start_i][start_j]
        waiting.append([start_i+dir[i][0],start_j+dir[i][1]])
    while len(waiting) > 0:
        cur_i,cur_j = waiting.popleft()
        for j in range(4):
            if grid[cur_i+dir[j][0]][cur_j+dir[j][1]] != inf and grid[cur_i+dir[j][0]][cur_j+dir[j][1]] < grid[cur_i][cur_j]:
                ans[cur_i+dir[j][0]][cur_j+dir[j][1]] += ans[cur_i][cur_j]
                waiting.append([cur_i+dir[j][0],cur_j+dir[j][1]])
print(ans)
s = 0
for i in range(1,H+1):
    for j in range(1,W+1):
        s += ans[i][j]
print(s)
#2022/8/8 00:56:17