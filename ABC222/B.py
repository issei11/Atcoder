N, P = map(int,input().split())
a = list(map(int,input().split()))+[1000]
a.sort()
i = 0
cnt = 0
while a[i] < P :
    i += 1
    cnt += 1

print(cnt)
#2022/5/8 00:03:32