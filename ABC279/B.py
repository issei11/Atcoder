S = input()
T = input()

if len(S) < len(T):
    print("No")
    exit()
s = len(S)
t = len(T)
for i in range(s-t+1):
    c = 0
    for j in range(t):
        if S[i+j] == T[j]:
            c += 1
    if c == t:
        print("Yes")
        exit()
print("No")