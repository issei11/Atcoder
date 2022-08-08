N,Q = map(int,input().split())
check = [0 for _ in range(N+1)]
ans = [0 for _ in range(N)]
for _ in range(Q):
    l,r = map(int,input().split())
    check[l-1] += 1
    check[r] -= 1
c = 0
for i in range(N):
    c += check[i]
    if c%2 == 1:
        ans[i] = 1
print(*ans,sep='')
#2022/8/8 00:08:12