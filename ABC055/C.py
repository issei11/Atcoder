N,M = map(int,input().split())

ans = 0
while True:
    if N >= 1 and M >= 2:
        n = N
        m = M//2
        a = min(n,m)
        N -= a
        M -= a*2
        ans += a
    elif M >= 4:
        m = M//4
        M -= m*4
        ans += m
    else:
        break
print(ans)
#2022/8/17 00:07:30