N = int(input())
S = []
T = []
c = ''.join(['.' for i in range(N)])
for i in range(N):
    s = input()
    if s != c:
        S.append(s)
for i in range(N):
    t = input()
    if t != c:
        T.append(t)

#Sの図形部分の長方形取り出し
c = ['.' for i in range(len(S))]
left_S = 0
right_S = N-1
for j in range(N):
    if [S[i][j] for i in range(len(S))] == c:
        left_S += 1
    else:
        break
for j in range(N):
    if [S[i][N-1-j] for i in range(len(S))] == c:
        right_S -= 1
    else:
        break

#Tの図形部分の長方形取り出し
c = ['.' for i in range(len(T))]
left_T = 0
right_T = N-1
for j in range(N):
    if [T[i][j] for i in range(len(T))] == c:
        left_T += 1
    else:
        break
for j in range(N):
    if [T[i][N-1-j] for i in range(len(T))] == c:
        right_T -= 1
    else:
        break

ans = 0
cnt = 0
#Sを0度回転または180度回転
if len(S) == len(T) and right_S-left_S+1 == right_T-left_T+1:
    for i in range(len(S)):
        for j in range(left_S,right_S+1):
            if S[i][j] == T[i][j-left_S+left_T]:
                cnt += 1
    if cnt == len(S)*(right_S-left_S+1):
        ans += 1
    cnt = 0
    for i in range(len(S)):
        for j in range(left_S,right_S+1):
            if S[i][j] == T[len(S)-1-i][right_T+left_S-j]:
                cnt += 1
    if cnt == len(S)*(right_S-left_S+1):
        ans += 1
    cnt = 0
#Sを90度回転または270度回転
if len(S) == right_T-left_T+1 and right_S-left_S+1 == len(T):
    for i in range(len(S)):
        for j in range(left_S,right_S+1):
            if S[i][j] == T[j-left_S][right_T-i]:
                cnt += 1
    if cnt == len(S)*(right_S-left_S+1):
        ans += 1
    cnt = 0
    for i in range(len(S)):
        for j in range(left_S,right_S+1):
            if S[i][j] == T[right_S-j][i+left_T]:
                cnt += 1
    if cnt == len(S)*(right_S-left_S+1):
        ans += 1
    cnt = 0

if ans:
    print('Yes')
else:
    print('No')
#2022/5/12 01:09:29