N, X = map(int,input().split())
A = [0]
B = [0]
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

C = [0]

sum = 0
for i in range(1,N+1):
    if A[i] <= B[i]:
        sum += A[i]
        C.append(B[i]-A[i])
    else:
        sum += B[i]
        C.append(A[i]-B[i])

C = sorted(C)

if sum > X:
    print('No')
elif sum == X:
    print('Yes')
else:
    K = X-sum
    dp = [[False for i in range(K+1)]for j in range(N+1)]
    dp[0][0] = True
    for i in range(1,N+1):
        for j in range(K+1):
            if j >= C[i]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-C[i]]
            else:
                dp[i][j] = dp[i-1][j]
    if dp[-1][-1]:
        print('Yes')
    else:
        print('No')
#2022/4/24 01:07:21