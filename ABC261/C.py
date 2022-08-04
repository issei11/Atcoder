N = int(input())
S_list = dict()
for i in range(N):
    S = input()
    if S not in S_list.keys():
        S_list[S] = 1
        print(S)
    else:
        print(S,'(',S_list[S],')',sep='')
        S_list[S] += 1