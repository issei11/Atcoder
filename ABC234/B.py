def dist2(x1,y1,x2,y2):
    return (x2-x1)**2+(y2-y1)**2

N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

d = []
dist = 0

for i in range(N):
    for j in range(N):
        dist = dist2(X[i],Y[i],X[j],Y[j])
        d.append(dist)

print((max(d))**0.5)

#2022/4/29 00:05:23