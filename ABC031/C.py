inf = float('inf')
N = int(input())
a = list(map(int,input().split()))
aoki = -inf
aoki_tmp = 0
takahashi_max = -inf
takahashi = -inf
takahashi_tmp = 0
for i in range(N):
    for j in range(N):
        if i < j:
            for k in range(i,j+1):
                if (k-i)%2 == 1:
                    aoki_tmp += a[k]
                else:
                    takahashi_tmp += a[k]
        elif i > j:
            for k in range(j,i+1):
                if (k-j)%2 == 1:
                    aoki_tmp += a[k]
                else:
                    takahashi_tmp += a[k]
        else:
            aoki_tmp = -inf
            takahashi_tmp = -inf
        if aoki < aoki_tmp:
            aoki = aoki_tmp
            takahashi = takahashi_tmp
        aoki_tmp = 0
        takahashi_tmp = 0
    if takahashi_max < takahashi:
        takahashi_max = takahashi
    takahashi = -inf
    aoki = -inf
print(takahashi_max)

#2022/8/7 00:39:08 3WA