N = int(input())
dp = [[0 for _ in range(5)] for _ in range(N)]
T = []
X = []
A = []
for _ in range(N):
    t,x,a = map(int,input().split())
    T.append(t)
    X.append(x)
    A.append(a)

dp[0][0] = 0
if T[0] >= X[0]:
    dp[0][X[0]] = A[0]

tmp = 0
for i in range(1,N):
    t = T[i]-T[i-1]
    for j in range(5):
        if T[i] >= j:
            if j == X[i]:
                for k in range(5):
                    if abs(j-k) <= t:
                        tmp = max(tmp,dp[i-1][k]+A[i])
            else:
                for k in range(5):
                    if abs(j-k) <= t:
                        tmp = max(tmp,dp[i-1][k])
            dp[i][j] = tmp
            tmp = 0
print(max(dp[N-1]))