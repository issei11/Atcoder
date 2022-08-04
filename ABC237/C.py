def kaibun(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True

S = input()
flag = True

if kaibun(S):
    print("Yes")
else:
    i = 0
    while S[i] == 'a':
        i += 1
    l = i+1
    j = 1
    while S[-j] == 'a':
        j += 1
    r = j
    if r < l:
        print('No')
    else:
        S = S.strip('a')
        if kaibun(S):
            print('Yes')
        else:
            print('No')
#2022/4/26 00:53:36