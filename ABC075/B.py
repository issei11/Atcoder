from re import S


H,W = map(int,input().split())
s = [input() for _ in range(H)]
S = [['.' for _ in range(W+2)] for _ in range(H+2)]
dir_i = [-1,-1,-1,0,0,1,1,1]
dir_j = [-1,0,1,-1,1,-1,0,1]
for i in range(H):
    for j in range(W):
        if s[i][j] == '.':
            S[i+1][j+1] = '.'
        elif s[i][j] == '#':
            S[i+1][j+1] = '#'
        cnt = 0
ans = [[0 for _ in range(W)] for _ in range(H)]
cnt = 0
for i in range(1,H+1):
    for j in range(1,W+1):
        for d in range(8):
            if S[i+dir_i[d]][j+dir_j[d]] == '#':
                cnt += 1
        if S[i][j] == '.':
            ans[i-1][j-1] = cnt
        elif S[i][j] == '#':
            ans[i-1][j-1] = '#'
        cnt = 0

for i in range(H):
    print(*ans[i],sep='')
#2022/8/27 00:22:09