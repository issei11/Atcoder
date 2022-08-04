heihoukonn = set()
for i in range(200):
    heihoukonn.add(i*i)

N,D = map(int,input().split())
X = []
for _ in range(N):
    x = list(map(int,input().split()))
    X.append(x)

ans = 0
dist2 = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(D):
            dist2 += (X[i][k]-X[j][k])**2
        if dist2 in heihoukonn:
            ans += 1
        dist2 = 0

print(ans)
#2022/7/15 00:10:42 1WA