n = int(input())
a = list(map(int,input().split()))

ans = 0
for x in a:
    cnt = 0
    while (x-cnt)%2 == 0 or (x-cnt)%3 == 2:
        cnt += 1
    ans += cnt
    cnt = 0
print(ans)
#2022/8/1 00:04:10