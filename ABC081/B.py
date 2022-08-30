N = int(input())
A = list(map(int,input().split()))
ans = 10**9
for i in range(N):
    j = 0
    while A[i]%2 == 0:
        A[i] = A[i]//2
        j += 1
    ans = min(j,ans)
print(ans)
#2022/8/30 00:03:07