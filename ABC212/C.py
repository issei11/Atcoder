N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
m = abs(A[0]-B[0])
i = 0
j = 0

while i < N and j < M:
    m = min(m,abs(A[i]-B[j]))
    if m == 0:
        break
    if A[i] > B[j]:
        j += 1
    elif A[i] < B[j]:
        i += 1
print(m)

#2022/6/3 00:25:34