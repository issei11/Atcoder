N = int(input())
A = list(map(int,input().split()))

angle = [False]*360

angle[0] = True

tmp = 0

for i in A:
    tmp = (tmp+i) % 360
    angle[tmp] = True

cnt = 0
cnt_l = []

for i in range(361):
    if angle[i%360] == True:
        cnt_l.append(cnt+1)
        cnt = 0
    else:
        cnt += 1

print(max(cnt_l))

#2022/4/26 00:09:08