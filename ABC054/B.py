N,M = map(int,input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]
for i in range(N-M+1):
    for j in range(N-M+1):
        cnt = 0
        for i1 in range(M):
            for j1 in range(M):
                if A[i+i1][j+j1] == B[i1][j1]:
                    cnt += 1
        if cnt == M**2:
            print('Yes')
            exit()
print('No')
#2022/8/16 00:08:11