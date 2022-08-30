N,K = map(int,input().split())
A = list(map(int,input().split()))

d = dict()
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
n = len(d)
ans = 0
d = sorted(d.items(),key=lambda x:x[1])
i = 0
while n > K:
    ans += d[i][1]
    n -= 1
    i += 1
print(ans)
#2022/8/30 00:09:09