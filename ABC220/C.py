N = int(input())
A = list(map(int,input().split()))
X = int(input())

sumA = sum(A)
tmp = X
a = tmp//sumA
tmp -= a*sumA
k = a*N
i = 0
while tmp >= 0:
    tmp -= A[i]
    i += 1
    k += 1

print(k)
#2022/5/9 00:14:53 + 2ペナ