W = int(input())
N = 23
print(N)
A = [0]*23
A[0] = 1
A[1] = 2
A[2] = 4
for i in range(3,23):
    A[i] = A[i-1]+A[i-2]+A[i-3]
print(*A)