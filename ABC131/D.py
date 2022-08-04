N = int(input())
l = []
for _ in range(N):
    a,b = map(int,input().split())
    l.append([b,a])

l.sort()

s = 0
cnt = 0
for i in range(N):
    s += l[i][1]
    if l[i][0] < s:
        break
    cnt += 1

print('Yes' if cnt >= N else 'No')
#2022/7/15 00:11:30