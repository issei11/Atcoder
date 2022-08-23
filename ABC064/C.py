N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    A[i] = A[i]//400
check = [0 for _ in range(9)]
for a in A:
    if a < 9:
        check[a] += 1
    else:
        check[8] += 1
ans = [0,0]
for i in range(9):
    if i != 8:
        if check[i] > 0:
            ans[0] += 1
            ans[1] += 1
    else:
        ans[1] += check[8]
if ans[0] == 0:
    ans[0] += 1
print(*ans)

#2022/8/23 00:12:15 1RE 1WA