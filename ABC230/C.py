N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())

L = ['.']*(S-R+1)

for i in range(P,Q+1):
    for j in range(R,S+1):
        if (i-j) == (A-B) or (i+j) == (A+B):
            L[j-R] = '#'
    print(''.join(L))
    L = ['.']*(S-R+1)
#2022/5/3 00:32:22