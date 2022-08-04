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

N,M = map(int,input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    u,v,l = map(int,input().split())
    edge[u-1].append([v-1,l])
    edge[v-1].append([u-1,l])

ans = []
for i in range(len(edge[0])):
    L = edge[0][i][1]
    edge[0][i][1] = float('inf')
    edge[edge[0][i][0]].sort()
    edge[edge[0][i][0]][0][1] = float('inf')
    d = dijkstra_heap(N,edge,0)
    ans.append(d[edge[0][i][0]]+L)
    edge[0][i][1] = L
    edge[edge[0][i][0]][0][1] = L

print(-1 if min(ans) == float('inf') else min(ans))

#2022/8/4 00:57:24 1TLE 2WA