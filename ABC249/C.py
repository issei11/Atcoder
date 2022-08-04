import itertools

N,K = map(int,input().split())

S = []

for i in range(N):
    s = input()
    S.append(s)

A = [0]*26
cnt = 0
cnt_max = 0
sum = 'A'

for i in range(1,N+1):#i個選ぶとき
    L = list(itertools.combinations(range(N), i))
    for j in range(len(L)):#i個の時、全パターン試す
        for k in range(i):
            sum += S[L[j][k]]
        A[0] = sum.count('a')
        A[1] = sum.count('b')
        A[2] = sum.count('c')
        A[3] = sum.count('d')
        A[4] = sum.count('e')
        A[5] = sum.count('f')
        A[6] = sum.count('g')
        A[7] = sum.count('h')
        A[8] = sum.count('i')
        A[9] = sum.count('j')
        A[10] = sum.count('k')
        A[11] = sum.count('l')
        A[12] = sum.count('m')
        A[13] = sum.count('n')
        A[14] = sum.count('o')
        A[15] = sum.count('p')
        A[16] = sum.count('q')
        A[17] = sum.count('r')
        A[18] = sum.count('s')
        A[19] = sum.count('t')
        A[20] = sum.count('u')
        A[21] = sum.count('v')
        A[22] = sum.count('w')
        A[23] = sum.count('x')
        A[24] = sum.count('y')
        A[25] = sum.count('z')
        for l in range(26):
            if A[l] == K:
                cnt += 1
            A[l] = 0
        sum = 'A'
        if cnt_max < cnt:
            cnt_max = cnt
        cnt = 0

print(cnt_max)