N = int(input())
C = []
for _ in range(N):
    C.append(int(input()))
C = sorted(C,reverse=True)

ans = 0
cnt = 0
p = [0 for _ in range(N)]
for i in range(N):
    if i > 0 and C[i] == C[i-1]:
        p[i] = p[i-1]
        ans += p[i]
        continue
    for j in range(i+1,N):
        if C[i]%C[j] == 0:
            cnt += 1
    if cnt > 0:
        p[i] = (cnt//2+1)/(cnt+1)
        ans += p[i]
        cnt = 0
    else:
        p[i] = 1
        ans += p[i]
print(ans)
#2022/8/1 00:49:59 1WA