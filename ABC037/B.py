N,Q = map(int,input().split())
ans = [0 for i in range(N)]
for _ in range(Q):
    l,r,t = map(int,input().split())
    for i in range(l-1,r):
        ans[i] = t
for i in range(N):
    print(ans[i])
#2022/8/8 00:02:59