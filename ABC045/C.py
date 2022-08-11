S = input()
S = S[::-1]
N = len(S)-1
ans = 0
cnt = 1
for i in range(1<<N):
    ans += int(S[0])
    for j in range(N):
        if (i>>j)&1:
            ans += int(S[j+1])
            cnt = 1
        else:
            ans += int(S[j+1])*10**cnt
            cnt += 1
    cnt = 1
print(ans)
#2022/8/11 00:15:09