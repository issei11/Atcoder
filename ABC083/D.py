S = input()
N = len(S)
ans = (N+1)//2
if N%2 == 0:
    i = 0
    check = set()
    while i < N//2:
        check.add(S[N//2-i-1])
        check.add(S[N//2+i])
        if len(check) == 2:
            break
        i += 1
    print(ans+i)
else:
    i = 0
    check = set(S[N//2])
    while i < N//2:
        check.add(S[N//2-i-1])
        check.add(S[N//2+i+1])
        if len(check) == 2:
            break
        i += 1
    print(ans+i)
#2022/8/30 00:28:19 3TLE