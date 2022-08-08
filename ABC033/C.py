S = input()

ans = 0
check_0 = False
for i in range(len(S)):
    if S[i] == '0':
        check_0 = True
    if S[i] == '+':
        if check_0 == False:
            ans += 1
        else:
            check_0 = False

if check_0 == False:
    print(ans+1)
else:
    print(ans)
#2022/8/8 00:08:04