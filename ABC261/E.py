N,C = map(int,input().split())
size = 30
X = C
TF_list = [[[0,1] for i in range(N+1)] for j in range(size)]
for i in range(1,N+1):
    T,A = map(int,input().split())
    #下の桁からやっていかないとどこまでやるべきかわからない。
    A = bin(A)
    j = 1
    while j < size+1:
        if A[-j] == 'b':
            break
        else:
            if T == 1: #and
                TF_list[j-1][i][0] = TF_list[j-1][i-1][0]&int(A[-j])
                TF_list[j-1][i][1] = TF_list[j-1][i-1][1]&int(A[-j])
            elif T == 2: #or
                TF_list[j-1][i][0] = TF_list[j-1][i-1][0]|int(A[-j])
                TF_list[j-1][i][1] = TF_list[j-1][i-1][1]|int(A[-j])
            elif T == 3: #xor
                TF_list[j-1][i][0] = TF_list[j-1][i-1][0]^int(A[-j])
                TF_list[j-1][i][1] = TF_list[j-1][i-1][1]^int(A[-j])
        j += 1
    while j < size+1:
        if T == 1: #and
            TF_list[j-1][i][0] = TF_list[j-1][i-1][0]&0
            TF_list[j-1][i][1] = TF_list[j-1][i-1][1]&0
        elif T == 2: #or
            TF_list[j-1][i][0] = TF_list[j-1][i-1][0]|0
            TF_list[j-1][i][1] = TF_list[j-1][i-1][1]|0
        elif T == 3: #xor
            TF_list[j-1][i][0] = TF_list[j-1][i-1][0]^0
            TF_list[j-1][i][1] = TF_list[j-1][i-1][1]^0
        j += 1

for i in range(1,N+1):
    X = bin(X)
    l = len(X)-2
    ans = 0
    for j in range(l):
        ans += TF_list[l-1-j][i][int(X[j+2])]*2**(l-j-1)
    print(ans)
    X = ans
    ans = 0