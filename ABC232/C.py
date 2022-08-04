import itertools

N,M = map(int,input().split())
A = []
B = []
C = []
D = []
for i in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
for i in range(M):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)

ptn = list(itertools.permutations(list(range(1,N+1))))
P = list(range(1,N+1))
cnt = 0
flag = False
for p in ptn:#各順列パターンptnについて
    for i in range(M):
        for j in range(M):
            if {p[A[i]-1],p[B[i]-1]} == {C[j],D[j]}:
                cnt += 1
    if cnt == M:
        print('Yes')
        flag = True
        break
    cnt = 0

if not flag:
    print('No')

#2022/5/1 00:29:04