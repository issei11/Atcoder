H,W = map(int,input().split())
A = [[0]*(W+1)]
row_sum = [0]
col_sum = [0]
for i in range(1,H+1):
    A_i = [0] + list(map(int,input().split()))
    A.append(A_i)
    row_sum.append(sum(A_i))

sum = 0
for j in range(1,W+1):
    for i in range(1,H+1):
        sum += A[i][j]
    col_sum.append(sum)
    sum = 0

ans = [0]*W
a = 0
for i in range(1,H+1):
    for j in range(1,W+1):
        ans[j-1] = row_sum[i]+col_sum[j]-A[i][j]
    print(*ans)
    ans = [0]*W