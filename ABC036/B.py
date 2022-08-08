N = int(input())
ans = [[0 for j in range(N)]for i in range(N)]
for i in range(N):
    s = input()
    for j in range(N):
        ans[j][N-1-i] = s[j]
for i in range(N):
    print(*ans[i],sep='')