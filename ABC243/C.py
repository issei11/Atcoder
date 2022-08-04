N = int(input())
P = [[-1,-1]]
for i in range(N):
    x, y = map(int,input().split())
    p = [y,x]
    P.append(p)
S = list(input())
for i in range(1,N+1):
    P[i].append(S[i-1])

P_s = sorted(P)

i = 1
flag = 0
#print(P_s)

while i < N:
    if P[i][2] == 'R':
        for j in range(i+1,N+1):
            if P[j][2] == 'L' and P[i][0] ==  P[j][0]:
                print('Yes')
                i += N
                flag += 1
    i += 1

if flag == 0:
    print('No')

#2022/4/19 01:03:30 無理