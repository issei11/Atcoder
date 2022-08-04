N = int(input())
C = [0]
P = [0]
for i in range(N):
    c,p = map(int,input().split())
    C.append(c)
    P.append(p)

#累積和
s = [[0,0]]
sum_1 = 0
sum_2 = 0
for i in range(1,N+1):
    if C[i] == 1:
        sum_1 += P[i]
        s.append([sum_1,sum_2])
    else:
        sum_2 += P[i]
        s.append([sum_1,sum_2])

Q = int(input())
for i in range(Q):
    query = list(map(int,input().split()))
    print(*[s[query[1]][0]-s[query[0]-1][0],s[query[1]][1]-s[query[0]-1][1]])