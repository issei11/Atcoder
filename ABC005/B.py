N = int(input())
ans = float('inf')
for _ in range(N):
    T = int(input())
    if T < ans:
        ans = T
print(ans)
#2022/7/23 00:01:29