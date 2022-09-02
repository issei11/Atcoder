N,M = map(int,input().split())
if N >= 3 and M >= 3:
    print((N-2)*(M-2))
else:
    if N >= 2 and M >= 2:
        print(0)
    else:
        if N == 1 and M == 1:
            print(1)
        elif N == 1:
            print(M-2)
        elif M == 1:
            print(N-2)
#2022/9/2 00:08:58