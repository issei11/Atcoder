S = input()
atcoder = 'atcoder'
S_tmp = ''
ans = 0
tmp = 0
for i in range(7):
    for j in range(7):
        if S[j] == atcoder[i]:
            S_tmp = S[:i] + S[j] + S[i:j] + S[j+1:]
            S = S_tmp
            ans += j-i
            break
print(ans)
