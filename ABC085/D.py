N,H = map(int,input().split())

sword = []
for _ in range(N):
    a,b = map(int,input().split())
    sword.append([a,0])
    sword.append([b,1])
sword = sorted(sword,reverse=True)

ans = 0
i = 0
while True:
    if sword[i][1] == 0:
        ans += (H+sword[i][0]-1)//sword[i][0]
        break
    else:
        ans += 1
        H -= sword[i][0]
        if H <= 0:
            break
        i += 1
print(ans)
#2022/8/30 00:21:07