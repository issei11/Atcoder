S = input()
cnt = 0
if len(S) < 4:
    if S == 'oo' or S == 'xxx' or S == 'xoo' or S == 'oxo' or S == 'oox' or S == 'ooo':
        print('No')
    else:
        print('Yes')
else:
    if S[:2] == 'xx':
        for i in range(len(S)):
            if i%3 == 2:
                if S[i] == 'o':
                    cnt += 1
            else:
                if S[i] == 'x':
                    cnt += 1
    elif S[:2] == 'xo':
        for i in range(len(S)):
            if i%3 == 1:
                if S[i] == 'o':
                    cnt += 1
            else:
                if S[i] == 'x':
                    cnt += 1
    elif S[:2] == 'ox':
        for i in range(len(S)):
            if i%3 == 0:
                if S[i] == 'o':
                    cnt += 1
            else:
                if S[i] == 'x':
                    cnt += 1
    if cnt == len(S):
        print('Yes')
    else:
        print('No')
#2022/5/3