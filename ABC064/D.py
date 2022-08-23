from collections import deque

N = int(input())
S = input()
i = 0
ans = deque()
l = 0
r = 0
while i < N:
    if S[i] == '(':
        l += 1
    else:
        r += 1
    if l >= r:
        ans.append(S[i])
    else:
        ans.appendleft('(')
        ans.append(S[i])
        l += 1
    i += 1
for j in range(l-r):
    ans.append(')')
print(*ans,sep='')
#2022/8/23 00:15:02