N = int(input())
T = list(map(int,input().split()))
T = [0] + T

A = [0]

for i in range(1,N+1):
    if i == 1:
        A.append(2**T[i])
    else:
        tmp = 2**T[i]
        a = 2**T[i]
        j = A[i-1]//(2*a)
        while tmp <= A[i-1]:
            tmp = 2*a*j + a
            j += 1
        A.append(tmp)

print(A[-1])

