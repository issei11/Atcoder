from collections import deque

R,C = map(int,input().split())
sy,sx = map(int,input().split())
sy -= 1
sx -= 1
gy,gx = map(int,input().split())
gy -= 1
gx -= 1
map = []
for _ in range(R):
    m = input()
    map.append(m)

my = [-1,0,1,0]
mx = [0,-1,0,1]

inf = float('inf')
dist = [[-1 for j in range(C)] for i in range(R)]
dist[sy][sx] = 0
waiting = deque()

for i in range(4):
    if map[sy+my[i]][sx+mx[i]] == '.':
        dist[sy+my[i]][sx+mx[i]] = dist[sy][sx] + 1
        waiting.append([sy+my[i], sx+mx[i]])

while len(waiting) > 0:
    cy,cx = waiting.popleft()
    for i in range(4):
        if map[cy+my[i]][cx+mx[i]] == '.' and dist[cy+my[i]][cx+mx[i]] == -1:
            dist[cy+my[i]][cx+mx[i]] = dist[cy][cx] + 1
            waiting.append([cy+my[i], cx+mx[i]])

print(dist[gy][gx])

#2022/7/29 01:13:40