N = int(input())
A = [0] + list(map(int,input().split()))

M = 0
M_idx = 0
booby = 0
b_idx = 0
for i in range(1,N+1):
    if A[i] > M:
        booby = M
        b_idx = M_idx
        M = A[i]
        M_idx = i
    elif A[i] > booby:
        booby = A[i]
        b_idx = i

print(b_idx)
#2022/6/2 00:08:51