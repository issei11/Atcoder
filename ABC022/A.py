N,S,T = map(int,input().split())
W = int(input())
ans = 0
for _ in range(N-1):
    if S <= W and W <= T:
        ans += 1
    W += int(input())
if S <= W and W <= T:
    ans += 1
print(ans)
#2022/8/4 00:02:38