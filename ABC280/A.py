H,W = map(int,input().split())
cnt = 0
for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == '#':
            cnt += 1
print(cnt)