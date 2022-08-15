N = int(input())
n = 2*10**5+2
num = [0 for _ in range(n)]

for _ in range(N):
    L,R = map(int,input().split())
    num[L] += 1
    num[R] -= 1

left = 0
right = 0
ans = []
for i in range(n):
    if num[i] > 0:
        if left == right:
            ans.append(i)
        left += num[i]
    elif num[i] < 0:
        if left == right-num[i]:
            ans.append(i)
            print(*ans)
            ans = []
        right -= num[i]
