N,T = map(int,input().split())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)
ans = 0
for i in range(N-1):
    if A[i+1]-A[i] <= T:
        ans += A[i+1]-A[i]
    else:
        ans += T
print(ans+T)
#2022/8/5 00:08:37