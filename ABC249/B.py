S = input()

S_swap = S.swapcase()
S_lower = S.lower()
S_upper = S.upper()

flag = 0

if S_lower != S_swap:
    flag += 1
if S_upper != S_swap:
    flag += 1

for i in range(len(S)):
    a = S.count(S[i])
    if a > 1:
        flag += 1

if flag == 2:
    print('Yes')
else:
    print('No')