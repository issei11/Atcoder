S = input()
T = input()
if len(S)>len(T):
    print('No')
    exit()
if S == T[:len(S)]:
    print('Yes')
else:
    print('No')