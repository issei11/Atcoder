from collections import deque
import sys
sys.setrecursionlimit(1000000)

tour = []
def eulertour(cur_node, prev_node):
    # 初めてノードを通るときに記録
    tour.append(cur_node+1)
    for next_node in edges[cur_node]:
        if next_node != prev_node: 
            eulertour(next_node, cur_node)
            # 戻ってきて通るときに記録
            tour.append(cur_node+1)


n,x,y = map(int,input().split())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    u,v = map(int,input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

eulertour(x-1,x-1)
ans = deque()
ans_set = set()
for i in range(len(tour)):
    if tour[i] not in ans_set:
        ans.append(tour[i])
        ans_set.add(tour[i])
        if tour[i] == y:
            print(*ans)
            exit()
    else:
        j = -1
        while ans[j] != tour[i]:
            m = ans.pop()