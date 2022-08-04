T = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

if N < M:
    print('no')
else:
    cnt = 0
    j = 0
    for i in range(M):
        while j < N:
            if A[j] <= B[i] <= A[j]+T:
                cnt += 1
                j += 1
                break
            else:
                j += 1
    print('yes' if cnt == M else 'no')

#2022/7/23 00:07:49