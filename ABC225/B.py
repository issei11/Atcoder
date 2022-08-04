N = int(input())
A = []
B = []
for i in range(1,N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

cnt = 0
star = 0
if A[0] == A[1] or A[0] == B[1]:
    star = A[0]
    for i in range(2,N-1):
        if star == A[i] or star == B[i]:
            cnt += 1
elif B[0] == B[1] or B[0] == A[1]:
    star = B[0]
    for i in range(2,N-1):
        if star == A[i] or star == B[i]:
            cnt += 1

if cnt == N-3:
    print('Yes')
else:
    print('No')

#2022/5/6 00:12:03