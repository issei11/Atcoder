H,W = map(int,input().split())
S = [[0 for _ in range(H)] for _ in range(W)]
T = [[0 for _ in range(H)] for _ in range(W)]
for i in range(H):
    s = input()
    for j in range(W):
        S[j][i] = s[j]
for i in range(H):
    t = input()
    for j in range(W):
        T[j][i] = t[j]
if sorted(S) == sorted(T):
    print("Yes")
else:
    print("No")