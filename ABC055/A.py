N = int(input())
ans = 0
for i in range(1,N+1):
    ans += 800
    if i%15 == 0:
        ans -= 200
print(ans)
#2022/8/17 00:01:52