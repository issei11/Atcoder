L1,R1,L2,R2 = map(int,input().split())
l = [0]*101
for i in range(L1,R1+1):
    l[i] += 1
for i in range(L2,R2+1):
    l[i] += 1
ans = 0
for i in range(len(l)):
    if l[i] == 2:
        ans += 1
if ans > 0:
    print(ans-1)
else:
    print(ans)