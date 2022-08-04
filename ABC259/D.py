from collections import deque

def bfs(edges,start,end):
    if start == end:
        return True
    waiting = deque()
    done = [0]*N
    done[start] = 2
    for n in edges[start]:
        done[n] = 1
        waiting.append(n)
    while len(waiting):
        cur_node = waiting.popleft()
        if done[cur_node] != 2:
            done[cur_node] = 2 # 訪問したので2
            if end == cur_node: 
                return True
            for n in edges[cur_node]:
                if done[n] == 0: # 初めて発⾒
                    done[n] = 1 # 未訪問なので1
                    waiting.append(n) # キュー追加
    return False

N = int(input())
sx,sy,tx,ty = map(int,input().split())

x = []
y = []
r = []
s = -1
t = -1
for i in range(N):
    X,Y,R = map(int,input().split())
    x.append(X)
    y.append(Y)
    r.append(R)

edges_list = [[] for _ in range(N)]

for i in range(N):
    if s == -1:
        if (x[i]-sx)**2+(y[i]-sy)**2 == r[i]**2:
            s = i
    if t == -1:
        if (x[i]-tx)**2+(y[i]-ty)**2 == r[i]**2:
            t = i
    for j in range(i+1,N):
        if (r[i]-r[j])**2 <= (x[i]-x[j])**2+(y[i]-y[j])**2 <= (r[i]+r[j])**2:
            edges_list[i].append(j)
            edges_list[j].append(i)

flag = bfs(edges_list,s,t)

print("Yes" if flag else "No")