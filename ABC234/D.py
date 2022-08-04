N,K = map(int,input().split())
P = list(map(int,input().split()))
sort = [i for i in range(1,N+1)]
ans = [N-K+1]

tmp = N-K+1

for i in range(1,N-K+1):
    sort[P[-i]-1] = 0
    if tmp > P[-i]:
        ans.append(tmp)
    elif tmp <= P[-i]:
        j = tmp-2
        tmp = sort[tmp-2]
        while tmp == 0:
            tmp = sort[j-1]
            j -= 1
        ans.append(tmp)


for i in range(1,N-K+2):
    print(ans[-i])
#2022/4/29 00:38:11