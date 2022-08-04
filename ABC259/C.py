S = input()
T = input()

s = []
t = []

s_child = []
t_child = []

for i in range(len(S)):
    if i == 0:
        s_child.append(S[i])
    else:
        if S[i] == S[i-1]:
            s_child.append(S[i])
        else:
            s.append(s_child)
            s_child = [S[i]]
s.append(s_child)

for i in range(len(T)):
    if i == 0:
        t_child.append(T[i])
    else:
        if T[i] == T[i-1]:
            t_child.append(T[i])
        else:
            t.append(t_child)
            t_child = [T[i]]
t.append(t_child)

cnt = 0
check = 10**9
if len(s) == len(t):
    check = len(s)
    for i in range(len(s)):
        if s[i] == t[i]:
            cnt += 1
        else:
            if 1 < len(s[i]) < len(t[i]):
                if s[i][0] == t[i][0]:
                    cnt += 1

print('Yes' if cnt == check else "No")