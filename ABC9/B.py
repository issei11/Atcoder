N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

A = sorted(A,reverse=True)

max2 = 0
for i in range(N):
    if A[i] != A[0]:
        max2 = A[i]
        break
print(max2)
#2022/8/1 00:06:53