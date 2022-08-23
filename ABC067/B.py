N,K = map(int,input().split())
l = list(map(int,input().split()))
l = sorted(l,reverse=True)
ans = 0
for i in range(K):
    ans += l[i]
print(ans)
#2022/8/23 00:01:55