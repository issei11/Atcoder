N,M = map(int,input().split())
e_list = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e_list[b].append(a)
    e_list[a].append(b)

for node in e_list[0]:
    for goal in e_list[node]:
        if goal == N-1:
            print('POSSIBLE')
            exit()
print('IMPOSSIBLE')
#2022/8/24 00:05:38