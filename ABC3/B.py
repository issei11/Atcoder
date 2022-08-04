S = input()
T = input()

flag = 0
check = {'a','t','c','o','d','e','r'}

for i in range(len(S)):
    if S[i] == T[i]:
        flag += 1
    else:
        if S[i] == '@' and T[i] in check:
            flag += 1
        elif T[i] == '@' and S[i] in check:
            flag += 1

if flag == len(S):
    print('You can win')
else:
    print('You will lose')

#2022/7/22 00:08:38