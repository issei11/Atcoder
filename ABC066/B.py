S = input()
N = len(S)
for i in range(N):
    S = S[:N-1-i]
    if len(S)%2 == 0:
        if S[:len(S)//2] == S[len(S)//2:]:
            break
print(len(S))
#2022/6/12 00:05:32