def janken(x,y):
    if x == y:
        return 'd'#draw
    elif x == 'G' and y == 'C' or x == 'C' and y == 'P' or x == 'P' and y == 'G':
        return 'x'#xの勝ち
    else:
        return 'y'#yの勝ち


N, M = map(int,input().split())
A = [[0]*(M+1)]

for i in range(2*N):
    Ai = [0] + list(input())
    A.append(Ai)

rank =[[-100000,0]]+ [[0,i] for i in range(1,2*N+1)]

for j in range(1,M+1):
    for i in range(1,N+1):
        #rank[2*i][1]とrank[2*i-1][1]が対決
        #A[rank[2*i][1]][j]とA[rank[2*i-1][1]][j]を比較
        result = janken(A[rank[2*i-1][1]][j],A[rank[2*i][1]][j])
        if result == 'x':
            rank[2*i-1][0] -= 1
        elif result == 'y':
            rank[2*i][0] -= 1
    rank.sort()

for i in range(1,2*N+1):
    print(rank[i][1])
#2022/5/8 00:24:06