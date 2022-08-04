S = input()
T = input()

s = []
t = []

cnt = 0
for i in range(len(S)-1):
    if S[i] == T[i]:
        cnt += 1
    else:
        if S[i+1] != T[i+1]:
            s.append(S[i])
            s.append(S[i+1])
            t.append(T[i])
            t.append(T[i+1])
if S[-1] == T[-1]:
    cnt += 1

if cnt == len(S):
    print("Yes")
elif cnt == len(S)-2 and len(s) == 2:
    if s == t[::-1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")

#2022/5/8 00:17:31+2pena