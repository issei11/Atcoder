N,W = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort(reverse=True)
ans = 0
for a,b in AB:
    t = min(W,b)
    ans += t*a
    W -= t

print(ans)