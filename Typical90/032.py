from itertools import permutations

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
M = int(input())
check = [tuple(map(int,input().split())) for _ in range(M)]
check = set(check)

ans = []

arr = [i for i in range(N)]
flag = 0

for p in permutations(arr):
    for i in range(N-1):
        if tuple([p[i]+1,p[i+1]+1]) in check or tuple([p[i+1]+1,p[i]+1]) in check:
            flag = 1
            break
    if flag == 1:
        flag = 0
        continue
    else:
        s = 0
        for i in range(N):
            s += A[p[i]][i]
        ans.append(s)
if len(ans) == 0:
    print(-1)
    exit()
print(min(ans))

#2022/9/20 00:17:23