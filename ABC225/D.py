from collections import deque

N,Q = map(int,input().split())
L = [[-1,i,-1]for i in range(N+1)]
ans = deque()
cnt = 1
i = 0
for i in range(Q):
    a = list(map(int,input().split()))
    if a[0] == 1:
        L[a[1]][2] = a[2]
        L[a[2]][0] = a[1]
    elif a[0] == 2:
        L[a[1]][2] = -1
        L[a[2]][0] = -1
    elif a[0] == 3:
        i = a[1]
        ans.append(L[i][1])
        while L[i][2] != -1:
            ans.append(L[i][2])
            i = L[i][2]
            cnt += 1
        i = a[1]
        while L[i][0] != -1:
            ans.appendleft(L[i][0])
            i = L[i][0]
            cnt += 1
        ans.appendleft(cnt)
        print(*ans)
        ans = deque()
        i = 0
        cnt = 1
#2022/5/6 00:44:55