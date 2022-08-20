n = int(input())
a = list(map(int,input().split()))

accu = [a[0]]
ans_1 = 0
if a[0] >= 0:
    ans_1 += a[0]+1
    accu[0] = -1
for i in range(1,n):
    tmp = accu[i-1]+a[i]
    if i%2 == 1:
        if tmp <= 0:
            ans_1 += 1-tmp
            tmp = 1
    else:
        if tmp >= 0:
            ans_1 += tmp+1
            tmp = -1
    accu.append(tmp)

accu = [a[0]]
ans_2 = 0
if a[0] <= 0:
    ans_2 += 1-a[0]
    accu[0] = 1
for i in range(1,n):
    tmp = accu[i-1]+a[i]
    if i%2 == 0:
        if tmp <= 0:
            ans_2 += 1-tmp
            tmp = 1
    else:
        if tmp >= 0:
            ans_2 += tmp+1
            tmp = -1
    accu.append(tmp)

print(min(ans_1,ans_2))
#2022/8/20 00:26:12