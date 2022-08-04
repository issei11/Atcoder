from stat import SF_APPEND


S = input()
T = input()

S_ascii = []
T_ascii = []
for i in range(len(S)):
    S_ascii.append(ord(S[i]))
    T_ascii.append(ord(T[i]))
    cnt = 1
for i in range(len(S)-1):
    if S_ascii[i]-T_ascii[i] == S_ascii[i+1]-T_ascii[i+1] or S_ascii[i]-T_ascii[i] == S_ascii[i+1]-T_ascii[i+1]+26 or S_ascii[i]-T_ascii[i]+26 == S_ascii[i+1]-T_ascii[i+1]:
        cnt += 1

if cnt == len(S):
    print('Yes')
else:
    print('No')

#2022/5/1 00:16:24