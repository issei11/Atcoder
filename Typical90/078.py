N,M = map(int,input().split())
L = [[i,0] for i in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    L[max(a,b)][1] += 1
cnt = 0
for i in range(N+1):
    if L[i][1] == 1:
        cnt += 1
print(cnt)