import heapq
N,T = map(int,input().split())
A = list(map(int,input().split()))

if N == 1:
    print(0)
    exit()

h = [A[0]]
heapq.heapify(h)
cost = []
for i in range(1,N):
    m = heapq.heappop(h)
    cost.append(A[i]-m)
    heapq.heappush(h,A[i])
    heapq.heappush(h,m)
cost.sort()
M = cost[-1]
i = -1
ans = 0
while i >= -N+1:
    if cost[i] == M:
        ans += 1
    i -= 1
print(ans)

#2022/8/12 00:35:30 2WA