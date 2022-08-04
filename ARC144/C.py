N,K = map(int,input().split())
if K*2 > N:
    print(-1)
else:
    ans = [0 for _ in range(N)]
    i = 1
    while i <= K:
        ans[i+K-1] = i
        i += 1
    while 








    j = 1
    x = 0
    while i <= N-K:
        if i <= K:
            ans[i-1] = i+K
            i += 1
        else:
            if i+2*K <= N:
                ans[i-1] = i-K
                ans[i+2*K-1] = i+K
                i += 1
                x += 1
            else:
                ans[i-1] = i+K
                i += 1
    while i <= N-x:
        ans[i-1] = x+j
        i += 1
        j += 1
    print(*ans)