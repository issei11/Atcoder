N,K = map(int,input().split())
a = list(map(int,input().split()))
s = sum(a[:K])
ans = s
for i in range(N-K):
    s = s + a[K+i] - a[i]
    ans += s
print(ans)
#2022/8/8 00:03:18