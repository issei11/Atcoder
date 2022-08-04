import heapq

def dijkstra_heap(V,e_list,s):#sからの最短距離の配列を返す
    inf = float('inf')
    done = [False]*V
    dist = [inf]*V
    dist[s] = 0
    node_heap = []
    heapq.heappush(node_heap,[dist[s],s])
    while node_heap:
        tmp = heapq.heappop(node_heap)
        cur_node = tmp[1]
        if not done[cur_node]:
            for e in e_list[cur_node]:
                if dist[e[0]] > dist[cur_node] + e[1]:
                    dist[e[0]] = dist[cur_node] + e[1]
                    heapq.heappush(node_heap,[dist[e[0]],e[0]])
        done[cur_node] = True
    return dist

ans = float('inf')

N,M = map(int,input().split())
edges_list = [[] for i in range(N)]
for _ in range(M):
    a,b,t = map(int,input().split())
    edges_list[a-1].append([b-1,t])
    edges_list[b-1].append([a-1,t])
for s in range(N):
    tmp = dijkstra_heap(N,edges_list,s)
    if ans > tmp:
        ans = tmp
print(ans)
#2022/7/22 00:20:46