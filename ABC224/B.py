H,W = map(int,input().split())
A = [[0]*(W+1)]
for i in range(1,H+1):
    A_i = [0] + list(map(int,input().split()))
    A.append(A_i)

flag = True
for i1 in range(1,H+1):
    for i2 in range(i1,H+1):
        for j1 in range(1,W+1):
            for j2 in range(j1,W+1):
                if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                    flag = False

print('Yes' if flag else 'No')
#2022/5/7 00:06:29