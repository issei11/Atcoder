N = int(input())
s = [int(input()) for _ in range(N)]
s = sorted(s)
ans = sum(s)
S = [s[i]%10 for i in range(N)]

if ans%10 != 0:
    print(ans)
    exit()
for i in range(N):
    if S[i]%10 != 0:
        print(ans-s[i])
        exit()
print(0)
#2022/8/23 00:08:49