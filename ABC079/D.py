inf = float('inf')
def WarshallFloyd(V,e_matrix):
    dist = e_matrix
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != inf and dist[k][j] != inf:
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    return dist

H,W = map(int,input().split())
c = [list(map(int,input().split())) for _ in range(10)]
A = [list(map(int,input().split())) for _ in range(H)]

d = WarshallFloyd(10,c)
ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] != -1:
            ans += d[A[i][j]][1]
print(ans)
#2022/8/29 00:14:29