import bisect

N,Q = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
l = len(A)

if l > 1:
    cul = []
    cul.append(sum(A)-A[0]*l)
    cul.append(cul[0]-(A[1]-A[0])*(l-1))
    tmp = 0
    for i in range(1,N-1):
        tmp = cul[i]-(A[i+1]-A[i])*(l-1-i)+(A[i]-A[i-1])*i
        cul.append(tmp)
    cul.append(cul[N-1]+(A[N-1]-A[N-2])*(l-1))

    for i in range(Q):
        X = int(input())
        idx = bisect.bisect_left(A,X)
        if idx == N:
            print(cul[idx] + (X-A[idx-1])*(idx))
        elif idx == 0:
            print(cul[idx] + (A[idx]-X)*(l-idx))
        else:
            print(cul[idx] + (X-A[idx-1])*(idx) + (A[idx]-X)*(l-idx))
else:
    for i in range(Q):
        X = int(input())
        print(abs(X-A[0]))