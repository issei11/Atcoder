N,M = map(int,input().split())
out_bit_list = [0 for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    out_bit_list[y] += (1 << x)

b = [[i,1<<i] for i in range(N)]

dp = [0] * (1 << N)
dp[0] = 1

for i in range(1<<N):
    for j in range(N):
        if (i & b[j][1]) == 0 and (i & out_bit_list[j]) == 0:
            dp[i | b[j][1]] += dp[i]

print(dp[-1])