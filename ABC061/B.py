N,M = map(int,input().split())
ans = [0 for i in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    ans[a] += 1
    ans[b] += 1
for i in range(1,N+1):
    print(ans[i])
#2022/8/21 00:02:18