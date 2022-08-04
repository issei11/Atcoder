N,X = map(int,input().split())
A = [0]+list(map(int,input().split()))

cnt = 0
C = [False]*(N+1)
i = X
while C[i] == False:
    C[i] = True
    cnt += 1
    i = A[i]

print(cnt)
#2022/5/4 0:04:21