s = input()
g = 0
p = 0
ans = 0
for i in range(len(s)):
    if s[i] == 'g':
        if p < g:
            ans += 1
            p += 1
        else:
            g += 1
    else:
        if p < g:
            p += 1
        else:
            ans -= 1
            g += 1
print(ans)
#2022/8/11 00:06:46