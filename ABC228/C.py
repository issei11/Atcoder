N,K = map(int,input().split())
P = []
for i in range(N):
    P_i = list(map(int,input().split()))
    sum = P_i[0]+P_i[1]+P_i[2]
    P.append(sum)
P_sort = sorted(P)
K_score = P_sort[-K]

k = 0
for i in range(N):
    if P[i]+300 >= K_score:
        print("Yes")
    else:
        print("No")