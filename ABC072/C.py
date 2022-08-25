N = int(input())
a = list(map(int,input().split()))
b = [a[i]-1 for i in range(N)]
c = [a[i]+1 for i in range(N)]

d = dict()
for i in range(N):
    if a[i] in d:
        d[a[i]] += 1
    else:
        d[a[i]] = 1
    if b[i] in d:
        d[b[i]] += 1
    else:
        d[b[i]] = 1
    if c[i] in d:
        d[c[i]] += 1
    else:
        d[c[i]] = 1
ans = 0
for i in d.keys():
    if d[i] > ans:
        ans = d[i]
print(ans)
#2022/8/26 00:10:45