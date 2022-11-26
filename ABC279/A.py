S = input()
ans = 0
for i in range(len(S)):
    if S[i] == 'v':
        ans += 1
    else:
        ans += 2
print(ans)