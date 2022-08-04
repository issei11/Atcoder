import bisect

N,K = map(int,input().split())
P = list(map(int,input().split()))

x = 0
check = [[0,0] for _ in range(N+1)]
eat = [-1 for _ in range(N+1)]
table = [P[0]]
check[P[0]][0] += 1
table2 = [False]

if K == 1:
    for i in range(N):
        print(P[i])
else:
    for i in range(1,N):#ターンはi+1
        if table[-1] < P[i]:
            table.append(P[i])
            table2.append(False)
            check[P[i]][0] += 1
        else:
            b = bisect.bisect_left(table,P[i])
            check[P[i]][0] = check[table[b]][0]+1
            check[P[i]][1] = table[b]
            table[b] = P[i]
            if check[P[i]][0] >= K:
                x = P[i]
                table2[b] = True
                print(i+1,table,table2)
                for j in range(K):
                    eat[x] = i+1
                    x = check[x][1]
                if b == len(table)-1:
                    table[b] = table[b-1]
                elif b == 0:
                    table[b] = 0
                    k = 0
                    while table2[b+k] == True:
                        table[b+k] = table[b]
                        k += 1
                else:
                    table[b] = table[b-1]
                    k = 1
                    while table2[b+k] == True:
                        table[b+k] = table[b]
                        k += 1
    for i in range(1,N+1):
        print(eat[i])