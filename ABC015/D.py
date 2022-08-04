import copy

W = int(input())
N,K = map(int,input().split())
A,B = [],[]
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

dp = [[0]*(W+1) for _ in range(K+1)]

prev_dp = [[0]*(W+1) for _ in range(K+1)]
next_dp = [[0]*(W+1) for _ in range(K+1)]
for k in range(1,K+1):
    for w in range(W+1):
        if w >= A[0]:
            prev_dp[k][w] = B[0]

for n in range(1,N):
    for k in range(1,K+1):
        for w in range(1,W+1):
            if w-A[n] >= 0:
                next_dp[k][w] = max(prev_dp[k][w],prev_dp[k-1][w-A[n]]+B[n])
            else:
                next_dp[k][w] = prev_dp[k][w]
    prev_dp = next_dp
    next_dp = [[0]*(W+1) for _ in range(K+1)]
print(prev_dp[K][W])

#2022/8/2 02:24:33 
#MLEが取れないため、他の人のコードを参考にした。