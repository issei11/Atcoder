N,M = map(int,input().split())
known = [set() for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    known[x-1].add(y-1)
    known[y-1].add(x-1)

total = 0
cnt = 0
gloup = []
for i in range(2**N):
    for j in range(N):
        if ((i>>j)&1):
            gloup.append(j)
    for j in gloup:
        for k in gloup:
            if j != k:
                if k in known[j]:
                    cnt += 1
    if cnt == len(gloup)*(len(gloup)-1):
        total = max(total,len(gloup))
    cnt = 0
    gloup = []
print(total)

#2022/7/22 00:20:01