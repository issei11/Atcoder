S = input()
a,b = map(int,input().split())

N = len(S)

A = []

for i in range(N):
    if i == a-1:
        A.append(S[b-1])
    elif i == b-1:
        A.append(S[a-1])
    else:
        A.append(S[i])

print("".join(A))
#2022/4/27 00:07:54