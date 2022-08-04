def f(x,A):#技xを習得するのに必要な技をlistで返す
    ans = []
    if A[x][1] == 0:
        return ans
    else:
        ans = A[x][2:]
        for i in range(2,A[x][1]+2):
            ans += f(A[x][i],A)
    return ans

N = int(input())
A = [[0]]
for i in range(N):
    A_i = list(map(int,input().split()))
    A.append(A_i)#A[i][0] = T_i, A[i][1] = K_i

A_ans = f(N,A)
T = 0
for i in set(A_ans):
    T += A[i][0]
print(T+A[N][0])