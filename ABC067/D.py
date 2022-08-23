from collections import deque

N = int(input())
e_list = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e_list[b].append(a)
    e_list[a].append(b)

root = 0
F = 1
done = [False for _ in range(N)]
done[0] = True
waiting = deque()
waiting.append(root)
while len(waiting) > 0:
    now = waiting.popleft()
    for node in e_list[now]:
        if node != N-1 and done[node] == False:
            F += 1
            waiting.append(node)
            done[node] = True

root = N-1
S = 1
done = [False for _ in range(N)]
done[N-1] = True
waiting = deque()
waiting.append(root)
while len(waiting) > 0:
    now = waiting.popleft()
    for node in e_list[now]:
        if node != 0 and done[node] == False:
            S += 1
            waiting.append(node)
            done[node] = True

b = S+F-N

F = F-b//2
S = S-(b-b//2)
print('Fennec' if F>S else 'Snuke')
#2022/8/23 00:57:38 2WA