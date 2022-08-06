S = input()
ans = [0]*6
s = 'ABCDEF'
for i in range(len(S)):
    for j in range(len(s)):
        if S[i] == s[j]:
            ans[j] += 1
print(*ans)
#2022/8/6 00:02:04