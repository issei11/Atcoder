N,C = map(int,input().split())
s = []
t = []
c = []
for _ in range(N):
    p,q,r = map(int,input().split())
    s.append(p-1)
    t.append(q)
    c.append(r-1)

time_table = [[0 for _ in range(C)] for _ in range(10**5+2)]

for i in range(N):
    time_table[s[i]][c[i]] += 1
    time_table[t[i]][c[i]] -= 1
for i in range(1,10**5+2):
    for j in range(C):
        time_table[i][j] += time_table[i-1][j]
for i in range(10**5+2):
    for j in range(C):
        if time_table[i][j]:
            time_table[i][j] = 1

ans = 0
for i in range(10**5+2):
    ans = max(ans,sum(time_table[i]))
print(ans)

#2022/8/30 01:05:48 2WA