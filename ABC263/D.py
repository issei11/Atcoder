N,L,R = map(int,input().split())
A = list(map(int,input().split()))
S = 0
sum_A = 0
sum_L = 0
max_x = 0
x = 0
for i in range(N):
    sum_A += A[i]
    sum_L += L
    if max_x < sum_A-sum_L:
        max_x = sum_A-sum_L
        x = i+1
sum_A = 0
sum_R = 0
max_y = 0
y = 0
for i in range(N):
    if x+i >= N:
        sum_A += L
    else:
        sum_A += A[N-1-i]
    if x+i >= N:
        sum_R += min(A[N-1-i],R)
    else:
        sum_R += R
    if max_y < sum_A-sum_R:
        max_y = sum_A-sum_R
        y = i+1
print(sum(A)-max_x-max_y)