N, M = map(int,input().split())
e_matrix = [[0 for j in range(N+1)] for i in range(N+1)]
for _ in range(M):
    U,V = map(int,input().split())
    e_matrix[U][V] = 1
    e_matrix[V][U] = 1

ans = 0
for a in range(1,N+1):
    for b in range(a+1,N+1):
        for c in range(b+1,N+1):
            if e_matrix[a][b] == 1 and e_matrix[b][c] == 1 and e_matrix[c][a] == 1:
                ans += 1
print(ans)