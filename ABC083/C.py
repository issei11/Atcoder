x,y = map(int,input().split())
ans = 0
tmp = x
while tmp <= y:
    tmp *= 2
    ans += 1
print(ans)
#2022/8/30 00:03:13