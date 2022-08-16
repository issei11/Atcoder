N,Q = map(int,input().split())
S = input()
cnt = 0
for _ in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        cnt += x
    if t == 2:
        print(S[x-1-cnt%N])