N,W = map(int,input().split())
v = []
w = []
for _ in range(N):
    x,y = map(int,input().split())
    v.append(x)
    w.append(y)

if sum(w) <= 200*1000+1:
    W = min(W,sum(w))
    dp = [[0]*(W+1) for _ in range(N)]
    for i in range(W+1):
        if w[0] <= i:
            dp[0][i] = v[0]
    for i in range(1,N):
        for j in range(W+1):
            if j >= w[i]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N-1][W])
elif sum(v) <= 200*1000+1:
    V = 200*1000+1
    dp = [[0]*(V+1) for _ in range(N)]
    for i in range(V+1):
        if w[0] <= W and i >= v[0]:
            dp[0][i] = w[0]
    for i in range(1,N):
        for j in range(V+1):
            if j >= v[i]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-v[i]]+w[i])
                if dp[i][j] > W:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N-1][V])
else:
    s_v = 0
    s_w = 0
    max_v = 0
    for i in range(2**N):
        for j in range(N):
            if (i >> j)&1:
                s_v += v[j]
                s_w += w[j]
        if max_v < s_v and s_w <= W:
            max_v = s_v
    print(max_v)

#2022/8/7 00:42:18