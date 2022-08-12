S = input()
N = len(S)
now = ''
if S[:5] == 'dream':
    now = 'dream'
elif S[:5] == 'erase':
    now = 'erase'
else:
    print('NO')
    exit()
i = 5
while i < N:
    if now == 'dream':
        if i+5 <= N and S[i:i+5] == 'dream':
            i += 5
            now = 'dream'
            continue
        elif i+2 <= N and S[i:i+2] == 'er':
            if i+5 < N and S[i:i+5] == 'erase':
                i += 5
                now = 'erase'
                continue
            else:
                i += 2
                now = 'dreamer'
                continue
    elif now == 'dreamer':
        if i+5 <= N and S[i:i+5] == 'dream':
            i += 5
            now = 'dream'
            continue
        elif i+5 <= N and S[i:i+5] == 'erase':
            i += 5
            now = 'erase'
            continue
    elif now == 'erase':
        if i+5 <= N and S[i:i+5] == 'dream':
            i += 5
            now = 'dream'
            continue
        elif i+5 <= N and S[i:i+5] == 'erase':
            i += 5
            now = 'erase'
            continue
        elif i+1 <= N and S[i:i+1] == 'r':
            i += 1
            now = 'eraser'
            continue
    elif now == 'eraser':
        if i+5 <= N and S[i:i+5] == 'dream':
            i += 5
            now = 'dream'
            continue
        elif i+5 <= N and S[i:i+5] == 'erase':
            i += 5
            now = 'erase'
            continue
    print('NO')
    exit()
print('YES')
#2022/8/12 00:23:23 1WA