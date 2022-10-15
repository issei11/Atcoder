N,S = map(int,input().split())
dp = [[0 for _ in range(10001)] for _ in range(N)]
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    if i == 0:
        dp[i][a] = 1
        dp[i][b] = 2
    if i > 0:
        for j in range(10001):
            if dp[i-1][j] > 0:
                dp[i][j+a] = 1
                dp[i][j+b] = 2
if dp[N-1][S] > 0:
    print('Yes')
    ans = []
    if dp[N-1][S] == 1:
        ans.append('H')
    else:
        ans.append('T')
    for i in range(N-1):
        if ans[-1] == 'H':
            S -= A[N-1-i]
            if dp[N-2-i][S] == 1:
                ans.append('H')
            else:
                ans.append('T')
        else:
            S -= B[N-1-i]
            if dp[N-2-i][S] == 1:
                ans.append('H')
            else:
                ans.append('T')
    print(*ans[::-1],sep='')
else:
    print('No')