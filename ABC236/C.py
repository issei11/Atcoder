N,M = map(int,input().split())
S = list(map(str,input().split()))
T = list(map(str,input().split()))

i = 0
j = 0
while i < N and j < M:
    if S[i] == T[j]:
        print("Yes")
        i += 1
        j += 1
    else:
        print("No")
        i += 1
#2022/4/27 00:13:29