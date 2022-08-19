n = int(input())
if n == 1:
    S = list(input())
    S.sort()
    print(*S,sep='')
    exit()
S = list(input() for _ in range(n))
s = set(S[0])
for i in range(1,n):
    s = s&set(S[i])
s = list(s)
ans = [float('inf') for _ in range(len(s))]
tmp = 0
for i in range(len(s)):
    for x in S:
        for j in range(len(x)):
            if s[i] == x[j]:
                tmp += 1
        ans[i] = min(ans[i],tmp)
        tmp = 0
a = []
for i in range(len(ans)):
    for j in range(ans[i]):
        a.append(s[i])
a.sort()
print(*a,sep='')
#2022/8/17 00:15:51