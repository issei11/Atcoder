N = int(input())
e_list = [[] for _ in range(N)]
for _ in range(N):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    e_list[u].append(v)
    e_list[v].append(u)

Q = int(input())
for _ in range(Q):
    x,y = map(int,input().split())
