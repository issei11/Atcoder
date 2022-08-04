N,P,Q = map(int,input().split())
A = list(map(int,input().split()))
AmodP = [i%P for i in A]

cnt = 0
for a in range(N-4):
    for b in range(a+1,N-3):
        for c in range(b+1,N-2):
            for d in range(c+1,N-1):
                for e in range(d+1,N):
                    if (((((((AmodP[a]*AmodP[b])%P)*AmodP[c])%P)*AmodP[d])%P)*AmodP[e])%P == Q:
                        cnt += 1
print(cnt)