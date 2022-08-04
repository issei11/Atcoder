N = int(input())
A = []
check_A = []
for _ in range(N):
    a = list(input())
    A.append(a)
    for i in range(N):
        check_A.append(a[i])

check = []
for j in range(N):
    for i in range(N):
        if A[i][j] == 'W':
            check.append('L')
        elif A[i][j] == 'L':
            check.append('W')
        else:
            check.append(A[i][j])

if check_A == check:
    print('correct')
else:
    print('incorrect')