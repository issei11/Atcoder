H,W = map(int,input().split())
S = [['#' for _ in range(W+2)]]
for _ in range(H):
    s = ['#']+list(input())+['#']
    S.append(s)
S.append(['#' for _ in range(W+2)])

dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [-1,0,1,-1,0,1,-1,0,1]

ans = [[0 for _ in range(W+2)] for _ in range(H+2)]
ans_check = [[0 for _ in range(W+2)] for _ in range(H+2)]

cnt = 0
for i in range(H+2):
    for j in range(W+2):
        if i == 0 or i == H+1 or j == 0 or j == W+1:
            ans[i][j] = '#'
        else:
            for k in range(9):
                if S[i+dx[k]][j+dy[k]] == '#':
                    cnt += 1
            if cnt == 9:
                ans[i][j] = '#'
            else:
                ans[i][j] = '.'
            cnt = 0

for i in range(H+2):
    for j in range(W+2):
                if i == 0 or i == H+1 or j == 0 or j == W+1:
                    ans[i][j] = '.'

for i in range(1,H+1):
    for j in range(1,W+1):
        ans_check[i][j] = '.'
        for k in range(9):
            if ans[i+dx[k]][j+dy[k]] == '#':
                ans_check[i][j] = '#'
                break

for i in range(H+2):
    for j in range(W+2):
                if i == 0 or i == H+1 or j == 0 or j == W+1:
                    ans_check[i][j] = '#'

if ans_check == S:
    print('possible')
    for i in range(1,H+1):
        print(*ans[i][1:W+1],sep='')
else:
    print('impossible')

#2022/8/8 00:30:19