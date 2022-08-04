N = int(input())
a = list(map(int,input().split()))
b = [[i,0] for i in range(N+1)]

ans = 0
for i in range(N):
    if a[i] > N:
        ans += 1
    else:
        b[a[i]][1] += 1

for i in range(N+1):
    if b[i][1] >= i:
        ans += b[i][1]-i
    else:
        ans += b[i][1]

print(ans)
#2022/7/15 00:17:59 