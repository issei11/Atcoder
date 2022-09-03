N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]
tmp = 0
ans = 0
for i in range(N):
    for j in range(N):
        if s[j] == s[i]:
            tmp += 1
    for j in range(M):
        if t[j] == s[i]:
            tmp -= 1
    ans = max(ans,tmp)
    tmp = 0
print(ans)
#2022/9/2 00:05:35