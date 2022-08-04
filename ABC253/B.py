H,W = map(int,input().split())
i1 = -1
j1 = -1
i2 = -1
j2 = -1
for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == 'o' and i1 == -1:
            i1 = i
            j1 = j
        elif S[j] == 'o' and i1 != -1:
            i2 = i
            j2 = j

print(abs(i1-i2)+abs(j1-j2))