s = input()

tmp = []
cnt = 0
for i in range(1,len(s)+1):
    if s[-i] == 'B':
        cnt += 1
    elif s[-i] == '0':
        if cnt > 0:
            cnt -= 1
        else:
            tmp.append(0)
    elif s[-i] == '1':
        if cnt > 0:
            cnt -= 1
        else:
            tmp.append(1)
ans = tmp[::-1]
print(*ans,sep='')
#2022/8/9 00:04:31