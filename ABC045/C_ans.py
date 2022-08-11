S = input()
S_in = S
N = len(S)-1
ans = 0
for i in range(1<<N):
    for j in range(N):
        if (i>>j)&1:
            S = S[:N-j]+'+'+S[N-j:]
    print(S)
    ans += eval(S)
    S = S_in
print(ans)