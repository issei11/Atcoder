N = int(input())
s = 0
x = 0
y = 0
for _ in range(N):
    t,nxt_x,nxt_y = map(int,input().split())
    if t-s < abs(nxt_x-x)+abs(nxt_y-y) or (t-s)%2 != (abs(nxt_x-x)+abs(nxt_y-y))%2:
        print('No')
        exit()
    x = nxt_x
    y = nxt_y
    s = t
print('Yes')
#2022/8/30 00:05:14