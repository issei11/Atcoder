S = input()
ans = []
for i in range(2**3):
    for j in range(3):
        ans.append(S[j])
        if (i >> j)&1:
            ans.append('+')
        else:
            ans.append('-')
    ans.append(S[3])
    if eval(''.join(ans)) == 7:
        ans.append('=7')
        print(*ans,sep='')
        exit()
    ans = []
#2022/8/29 00:08:05