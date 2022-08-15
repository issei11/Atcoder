x = int(input())

ans = (x//11)*2
if 1 <= x%11 <= 6:
    ans += 1
elif x%11 > 6:
    ans += 2
print(ans)
#2022/8/15 00:06:24 1WA