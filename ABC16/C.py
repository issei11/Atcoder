N,M = map(int,input().split())
edges = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    edges[A][B] = 1
    edges[B][A] = 1

ftof = [0]*(N+1)
for i in range(1,N+1):
    for j in range(1,N+1):
        if edges[i][j] == 1:
            for k in range(1,N+1):
                if edges[j][k] == 1 and edges[i][k] == 0 and i != k and ftof[k] == 0:
                    ftof[k] = 1
    print(sum(ftof))
    ftof = [0]*(N+1)
#2022/8/3 00:20:20