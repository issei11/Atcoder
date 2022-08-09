N = int(input())
a = list(map(int,input().split()))
key_list = list(range(1,N+1))
d = dict(zip(key_list,a))
d_sorted = sorted(d.items(),key=lambda x:x[1],reverse=True)
for i in range(N):
    print(d_sorted[i][0])
#2022/8/9 00:08:38