N = int(input())
a = list(map(int,input().split()))
if sum(a)%N != 0:
    print(-1)
    exit()

num = sum(a)//N

s = 0
ans = 0
cnt = 0
for i in range(N):
    s += a[i]
    cnt += 1
    if s//cnt == num and s%cnt == 0:
        ans += cnt-1
        cnt = 0
        s = 0

print(ans)
#2022/8/6 00:07:21