N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append([a,i])
A.sort()
num = 0
ans = [0 for i in range(N)]
for i in range(1,N):
    if A[i][0] == A[i-1][0]:
        ans[A[i][1]] = num
    else:
        num += 1
        ans[A[i][1]] = num
for i in range(N):
    print(ans[i])
#2022/8/8 00:08:36