N = int(input())
K = int(input())
x = list(map(int,input().split()))

ans = 0
for i in range(N):
    ans += min(2*K-2*x[i],2*x[i])
print(ans)
#2022/8/26 00:04:44