N,Q = map(int,input().split())

ans = [[-1,0,1]]+[[i-1,i,i+1] for i in range(1,N+2)]#双方向連結リスト

for i in range(Q):
    x = int(input())
    if ans[x][2] != N+1:
        ans[ans[x][0]][2] = ans[x][2]
        ans[x][0],ans[ans[x][2]][2] = ans[ans[x][2]][2],ans[x][0]
        ans[ans[x][2]][0],ans[ans[x][2]][2] = ans[ans[x][2]][2],ans[ans[x][2]][0]
        ans[x][0],ans[x][2] = ans[x][2],ans[x][0]
        ans[ans[x][2]][0] = x
    else:
        x = ans[x][0]
        ans[ans[x][0]][2] = ans[x][2]
        ans[x][0],ans[ans[x][2]][2] = ans[ans[x][2]][2],ans[x][0]
        ans[ans[x][2]][0],ans[ans[x][2]][2] = ans[ans[x][2]][2],ans[ans[x][2]][0]
        ans[x][0],ans[x][2] = ans[x][2],ans[x][0]
        ans[ans[x][2]][0] = x

ANS = []
j = 0
for i in range(N):
    j = ans[j][2]
    ANS.append(j)
print(*ANS)