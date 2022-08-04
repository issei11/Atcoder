H,W,N = map(int,input().split())
A = [(0,0)]
B = [(0,0)]
for i in range(1,N+1):
    a,b = map(int,input().split())
    A.append((a,i))
    B.append((b,i))

A.sort()
B.sort()
A_ans = [0 for i in range(N+1)]
B_ans = [0 for i in range(N+1)]
j_A = 0
j_B = 0
for i in range(1,N+1):
    if i > 1 and A[i][0] == A[i-1][0]:
        j_A += 1
    if i > 1 and B[i][0] == B[i-1][0]:
        j_B += 1
    A_ans[A[i][1]] = i-j_A
    B_ans[B[i][1]] = i-j_B
for i in range(1,N+1):
    print(A_ans[i],B_ans[i])
#2022/6/2 00:19:35