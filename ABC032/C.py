N,K = map(int,input().split())
S = []
for _ in range(N):
    s = int(input())
    if s == 0:
        print(N)
        exit()
    S.append(s)
i = 0
j = 0
p = S[0]
max_length = 0
while True:
    if p <= K:
        if max_length < j-i+1:
            max_length = j-i+1
        j += 1
        if j < N:
            p *= S[j]
        else:
            break
    else:
        if j > i:
            p //= S[i]
            i += 1
        else:
            j += 1
            i += 1
            if j < N:
                p = S[j]
            else:
                break
print(max_length)

#2022/8/8 00:21:21