N,X,Y,Z = map(int,input().split())
a = [-1] + list(map(int,input().split()))
b = [-1] + list(map(int,input().split()))
c = [-1] + [a[i]+b[i] for i in range(1,N+1)]

A = [[a[i],i,False] for i in range(1,N+1)]
B = [[b[i],i,False] for i in range(1,N+1)]
C = [[c[i],i,False] for i in range(1,N+1)]

ans = []

pass_num = 1

for i in range(X):
    #pass_numの初期化
    pass_num = 1
    while C[pass_num-1][2] == True:
        pass_num += 1
    for j in range(N):
        if A[pass_num-1][0] < A[j][0] and A[j][2] == False:
            pass_num = j+1
    ans.append(pass_num)
    A[pass_num-1][2] = True
    B[pass_num-1][2] = True
    C[pass_num-1][2] = True

for i in range(Y):
    #pass_numの初期化
    pass_num = 1
    while C[pass_num-1][2] == True:
        pass_num += 1
    for j in range(N):
        if B[pass_num-1][0] < B[j][0] and B[j][2] == False:
            pass_num = j+1
    ans.append(pass_num)
    B[pass_num-1][2] = True
    C[pass_num-1][2] = True

for i in range(Z):
    #pass_numの初期化
    pass_num = 1
    while C[pass_num-1][2] == True:
        pass_num += 1
    for j in range(N):
        if C[pass_num-1][0] < C[j][0] and C[j][2] == False:
            pass_num = j+1
    ans.append(pass_num)
    C[pass_num-1][2] = True

ans.sort()
for ans_num in ans:
    print(ans_num)
