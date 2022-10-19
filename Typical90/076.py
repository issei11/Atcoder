N = int(input())
A = list(map(int,input().split()))

s = sum(A)

just = s//10
if just*10 != s:
    print('No')
    exit()

tmp = 0
for i in range(N):
    tmp += A[i]
    if tmp < s:
        A.append(A[i])
    else:
        A.append(A[i])
        break

N = len(A)
tmp = A[0]
i = 0
j = 0
while True:
    if tmp < just:
        j += 1
        if j >= N:
            break
        tmp += A[j]
    elif tmp > just:
        tmp -= A[i]
        i += 1
    else:
        print('Yes')
        exit()
print('No')