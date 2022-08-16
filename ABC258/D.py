N,X = map(int,input().split())
A = []
B = []
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

ans = float('inf')

A_sum = 0
B_sum = 0
B_min = float('inf')
tmp = 0
for i in range(min(N,X)):
    A_sum += A[i]
    B_sum += B[i]
    B_min = min(B_min,B[i])
    tmp = A_sum + B_sum + (X-1-i)*B_min
    ans = min(tmp,ans)
print(ans)