S = input()
T = int(input())
dist = 0
x = 0
y = 0
cnt = 0
if T == 1:
    for i in range(len(S)):
        if S[i] == 'L':
            x -= 1
        elif S[i] == 'R':
            x += 1
        elif S[i] == 'U':
            y += 1
        elif S[i] == 'D':
            y -= 1
        elif S[i] == '?':
            cnt += 1
    print(abs(x)+abs(y)+cnt)
elif T == 2:
    for i in range(len(S)):
        if S[i] == 'L':
            x -= 1
        elif S[i] == 'R':
            x += 1
        elif S[i] == 'U':
            y += 1
        elif S[i] == 'D':
            y -= 1
        elif S[i] == '?':
            cnt += 1
    dist = abs(x)+abs(y)
    if dist >= cnt:
        print(dist-cnt)
    else:
        if (cnt-dist)%2 == 0:
            print(0)
        else:
            print(1)
#2022/8/8 00:09:27