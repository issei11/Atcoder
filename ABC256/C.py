h1,h2,h3,w1,w2,w3 = map(int,input().split())
h = [h1,h2,h3]
w = [w1,w2,w3]
ans = 0
grid = [0 for _ in range(9)]
for i in range(1,min(h[0],w[0])-1):
    for j in range(1,h[0]-i):
        for k in range(1,w[0]-i):
            for l in range(1,min(h[1]-k,w[1]-j)):
                a = h[0]-i-j
                b = h[1]-k-l
                c = w[0]-i-k
                d = w[1]-j-l
                e1 = h[2]-c-d
                e2 = w[2]-a-b
                if e1 == e2 and e1>0:
                    ans += 1
print(ans)