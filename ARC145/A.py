N = int(input())
S = input()
S_inv = S[::-1]
if S == 'BA':
    print('No')
    exit()
if S_inv[0] == 'A':
    print('Yes')
elif S_inv[0] == 'B':
    if S[0] == 'B':
        print('Yes')
    else:
        print('No')