N = int(input())
l = [i for i in range(1,7)]
N = N%30
for i in range(N):
    l[i%5],l[i%5+1] = l[i%5+1],l[i%5]
print(*l,sep='')
#2022/7/22 00:07:35