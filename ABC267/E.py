import heapq

N,M = map(int,input().split())
A = list(map(int,input().split()))

edge = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[v].append(u)
    edge[u].append(v)

h = []
h_check = dict()
tmp = 0
for i in range(N):
    for v in edge[i]:
        tmp += A[v]
    h.append(tmp)
    h_check[i] = tmp
    tmp = 0
for i in range(N):
    x = heapq.heappop(h)