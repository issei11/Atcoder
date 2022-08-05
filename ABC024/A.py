A,B,C,K = map(int,input().split())
S,T = map(int,input().split())
ans = A*S+B*T
if S+T >= K:
    ans -= C*(S+T)
print(ans)
#2022/8/5 00:02:15