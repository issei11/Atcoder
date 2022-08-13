H1,W1 = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H1)]
H2,W2 = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(H2)]

C = [[] for _ in range(H2)]
cnt = 0





for i in range(H2-1):
    for j in range(W2-1):
        if C[i][j][0] != C[i][j+1][0]:
            print('No')
            exit()
        if C[i][j][1] != C[i+1][j][1]:
            print('No')
            exit()
print('Yes')