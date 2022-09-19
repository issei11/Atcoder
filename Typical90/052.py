N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
mod = 10**9+7
ans = 1
for i in range(N):
    s = sum(A[i])
    ans *= s
    ans %= mod
print(ans)

#2022/9/19 00:04:52