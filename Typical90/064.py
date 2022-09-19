N,Q = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    ans += abs(A[i]-A[i+1])
for _ in range(N):
    L,R,V = map(int,input().split())
    if L == 1 and R == N:
        print(ans)
    elif L == 1:
        A

#2022/9/19 00:00:00