A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

if ((A[1]-C[1])*(B[0]-A[0])+(A[1]-B[1])*(A[0]-C[0]))*((A[1]-C[1])*(D[0]-A[0])+(A[1]-D[1])*(A[0]-C[0])) < 0:
    if ((B[1]-D[1])*(A[0]-B[0])+(B[1]-A[1])*(B[0]-D[0]))*((B[1]-D[1])*(C[0]-B[0])+(B[1]-C[1])*(B[0]-D[0])) < 0:
        print('Yes')
        exit()
print('No')