N,Q = map(int,input().split())
d = dict()
for i in range(Q):
    T,A,B = map(int,input().split())
    if T == 1:
        key = str(A)+'to'+str(B)
        d[key] = 1
    if T == 2:
        key = str(A)+'to'+str(B)
        d[key] = 0
    if T == 3:
        key1 = str(A)+'to'+str(B)
        key2 = str(B)+'to'+str(A)
        if key1 in d and key2 in d:
            if d[key1] == 1 and d[key2] == 1:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
