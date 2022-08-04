N = int(input())
D = [[0 for _ in range(N+1)]]
for i in range(N):
    d = list(map(int,input().split()))
    D.append([0]+d)

#二次元の累積和を行う
S = [[0 for j in range(N+1)] for i in range(N+1)]
S[1][1] = D[1][1]
for i in range(2,N+1):
    S[i][1] = S[i-1][1] + D[i][1]
for j in range(2,N+1):
    S[1][j] = S[1][j-1] + D[1][j]
for i in range(2,N+1):
    for j in range(2,N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + D[i][j]

M = [0 for _ in range((N+1)*(N+1)+1)]
for i1 in range(N+1):
    for j1 in range(N+1):
        for i2 in range(i1+1,N+1):
            for j2 in range(j1+1,N+1):
                s = S[i2][j2] - S[i2][j1] - S[i1][j2] + S[i1][j1]
                if M[(i2-i1)*(j2-j1)] < s:
                    M[(i2-i1)*(j2-j1)] = s

for i in range(1,(N+1)*(N+1)+1):
    if M[i] < M[i-1]:
        M[i] = M[i-1]

Q = int(input())

for _ in range(Q):
    P = int(input())
    print(M[P])
