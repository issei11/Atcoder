N,K = map(int,input().split())
A = list(map(int,input().split()))
sum = 0
i = 0
j = 0
cnt = 0
while i < N:
    while sum < K:
        sum += A[i]
        i += 1
    if sum == K:
        cnt += 1
        sum += A[i]
        i += 1
    while sum > K:
        sum -= A[j]
        j += 1

while sum > K:
    sum -= A[j]
    j += 1
if sum == K:
    cnt += 1
print(cnt)