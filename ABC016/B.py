A,B,C = map(int,input().split())
if A+B == C:
    if A-B == C:
        print('?')
    else:
        print('+')
else:
    if A-B == C:
        print('-')
    else:
        print('!')
#2022/8/3 00:02:22