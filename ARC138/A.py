from numpy import sort


N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [0] + A
A_s = sorted(A)

sum = 0
sum_s = 0
for i in range(1,K+1):
    sum += A[i]
    sum_s += A_s[-i]

if sum == sum_s:
    print(-1)
else:

#give up 00:43:53