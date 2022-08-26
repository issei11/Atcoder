from itertools import permutations

def WarshallFloyd(V,e_matrix):
    dist = e_matrix
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != inf and dist[k][j] != inf:
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    return dist

inf = float('inf')
N,M,R = map(int,input().split())
r = list(map(int,input().split()))
e_matrix = [[inf for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    e_matrix[b][a] = c
    e_matrix[a][b] = c

d = WarshallFloyd(N,e_matrix)

ans = inf
tmp = 0
for p in list(permutations(r)):
    for i in range(R-1):
        tmp += d[p[i]-1][p[i+1]-1]
    ans = min(ans,tmp)
    tmp = 0
print(ans)
#2022/8/26 00:26:05