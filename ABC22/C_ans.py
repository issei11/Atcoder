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
edge_0 = []
for _ in range(M):
    u,v,l = map(int,input().split())
    if u > 1:
        edge[u-1].append([v-1,l])
        edge[v-1].append([u-1,l])
    else:
        edge_0.append([v-1,l])

x = 0
ans = []
d1 = []
d11 = []
for i in range(len(edge_0)):
    x = edge_0.pop(i)
    for j in range(len(edge_0)):
        edge[0].append(edge_0[j])
        edge[edge_0[j][0]].append([0,edge_0[j][1]])
    d = dijkstra_heap(N,edge,0)
    if i == 1:
        print(1,d)
        d1 = d
    if i == 11:
        print(11,d)
        d11 = d
    ans.append(d[x[0]]+x[1])
    edge_0.insert(i,x)
    edge[0] = []

print(d1 == d11)

print(-1 if min(ans) == float('inf') else min(ans))