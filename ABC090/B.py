A,B = map(int,input().split())
ans = 0
for i in range(A,B+1):
    s = str(i)
    if s == s[::-1]:
        ans += 1
print(ans)
#2022/9/2 00:01:59