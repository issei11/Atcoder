N,L = map(int,input().split())
ans = sum([i for i in range(L,L+N)])
if L > 0:
    print(ans-L)
elif L+N-1 < 0:
    print(ans-(L+N-1))
else:
    print(ans)

#2022/7/15 00:06:03