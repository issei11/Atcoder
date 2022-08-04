L,R = map(int,input().split())
S = input()

ans = []

for i in range(len(S)):
    if i < L-1 or R-1 < i:
        ans.append(S[i])
    else:
        ans.append(S[-i+L+R-2])

print(''.join(ans))
#2022/4/30 00:06:59