def f(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(M)]

for i in range(N):
    ans = 0
    ans_dist = float('inf')
    for j in range(M):
        tmp = f(A[i][0],A[i][1],B[j][0],B[j][1])
        if tmp < ans_dist:
            ans = j+1
            ans_dist = tmp
    print(ans)
#2022/8/17 00:06:42