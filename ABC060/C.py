N,T = map(int,input().split())
t = list(map(int,input().split()))
ans = 0
start = 0
end = T
for i in range(1,N):
    if t[i] <= end:
        end = t[i]+T
    else:
        ans += end-start
        start = t[i]
        end = t[i]+T
ans += end-start
print(ans)
#2022/8/20 00:06:24