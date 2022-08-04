N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

X = A

for i in range(1,N):
    x1 = abs(A[i]-A[i+1])
    x2 = abs(A[i]-B[i+1])
    x3 = abs(B[i]-A[i+1])
    x4 = abs(B[i]-B[i+1])
    if x1>K and x2>K and x3>K and x4>K:
        print("No")
        break

#2022/4/19 00:38:09 無理