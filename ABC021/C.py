from collections import deque
import heapq

def dijkstra_heap(V,e_list,s):#sからの最短距離の配列を返す
    inf = float('inf')
    done = [False]*V
    dist = [inf]*V
    cnt = [0]*V
    dist[s] = 0
    cnt[s] = 1
    node_heap = []
    heapq.heappush(node_heap,[dist[s],s])
    while node_heap:
        tmp = heapq.heappop(node_heap)
        cur_node = tmp[1]
        if not done[cur_node]:
            for e in e_list[cur_node]:
                if dist[e] >= dist[cur_node] + 1:
                    dist[e] = dist[cur_node] + 1
                    cnt[e] += cnt[cur_node]%mod
                    heapq.heappush(node_heap,[dist[e],e])
        done[cur_node] = True
    return dist,cnt

N = int(input())
a,b = map(int,input().split())
a -= 1
b -= 1
M = int(input())
edge = [[] for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    edge[x-1].append(y-1)
    edge[y-1].append(x-1)

mod = 10**9+7

d,c = dijkstra_heap(N,edge,a)

print(c[b])
#2022/8/4 00:34:39