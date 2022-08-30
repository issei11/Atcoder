n,a,b = map(int,input().split())
ans = 0
for i in range(1,n+1):
    i = str(i)
    s = sum(list(map(int,i)))
    if a <= s <= b:
        ans += int(i)
print(ans)
#2022/8/30 00:03:52