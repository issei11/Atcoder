N = int(input())
a = list(map(int,input().split()))

x = a[0]
y = sum(a)-a[0]
ans = abs(x-y)
for i in range(1,N-1):
    x += a[i]
    y -= a[i]
    ans = min(ans,abs(x-y))
print(ans)
#2022/8/23 00:03:31