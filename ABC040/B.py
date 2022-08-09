n =int(input())
x = 1
y = 1
ans = 10000000
while x*x <= n:
    y = n//x
    tmp = abs(y-x)+n-x*y
    if ans >= tmp:
        ans = tmp
    x += 1
print(ans)
#2022/8/9 00:06:21