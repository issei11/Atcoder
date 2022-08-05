N,D,K = map(int,input().split())
L,R = [],[]
for _ in range(D):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)
for _ in range(K):
    s,t = map(int,input().split())
    for i in range(D):
        if (L[i] <= s and s <= R[i]) and (L[i] <= t and t <= R[i]):
            print(i+1)
            break
        elif L[i] <= s and s <= R[i]:
            if t < L[i]:
                s = L[i]
            else:
                s = R[i]
#2022/8/5 00:13:31