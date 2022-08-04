N,X = map(int,input().split())

data = [[0]]#data[i][0] == L_i

for i in range(1,N+1):
    L = list(map(int,input().split()))
    data.append(L)

ans_list = []
ans_list_tmp = [1]

for i in range(1,N+1):
    for j in range(1,data[i][0]+1):
        for k in ans_list_tmp:
            ans_list.append(data[i][j]*k)
    ans_list_tmp = list(ans_list)
    ans_list = []

print(ans_list_tmp.count(X))

#2022/4/30 00:32:59