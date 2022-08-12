N,x = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    if a[i] > x:
        ans += a[i]-x
        a[i] = x
    if a[i]+a[i+1] > x:
        ans += a[i+1] - (x-a[i])
        a[i+1] = x-a[i]
print(ans)
#2022/8/12 00:05:06