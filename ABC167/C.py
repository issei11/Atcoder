N,M,X = map(int,input().split())
A = []
for _ in range(N):
    a = list(map(int,input().split())) # C = A[0]
    A.append(a)

skill = [0 for _ in range(M)]
ans = 10**9
tmp = 0
flag = 0
for i in range(2**N):
    for j in range(N):
        if (i >> j) & 1:
            tmp += A[j][0]
            for k in range(1,M+1):
                skill[k-1] += A[j][k]
    for k in range(M):
        if skill[k] >= X:
            flag += 1
    if flag >= M:
        if ans > tmp:
            ans = tmp
    flag = 0
    tmp = 0
    skill = [0 for _ in range(M)]

if ans == 10**9:
    print(-1)
else:
    print(ans)

#2022/7/15 00:17:28