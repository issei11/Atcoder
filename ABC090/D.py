N,K = map(int,input().split())
ans = 0

if  K != 0:
    for b in range(K+1,N+1):
        ans += ((N+1)//b)*(b-K)
        tmp = (N+1)%b
        ans += max(tmp-K,0)
    print(ans)
else:
    print(N**2)
#2022/9/2 00:32:54