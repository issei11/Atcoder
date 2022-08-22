import heapq

N,A,B = map(int,input().split())
h = [(-1)*int(input()) for _ in range(N)]
heapq.heapify(h)
m = heapq.heappop(h)
ans = 0
while m < ans*(-B):
    m = m+(A-B)
    heapq.heappush(h,m)
    m = heapq.heappop(h)
    ans += 1
print(ans)

#2022/8/23 00:23:08