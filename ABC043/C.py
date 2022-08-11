N = int(input())
A = list(map(int,input().split()))

d = [i**2 for i in range(300)]

s = 0
ans = float('inf')
for i in range(-100,101):
    for a in A:
        s += d[abs(a-i)]
    if ans > s:
        ans = s
    s = 0
print(ans)
#2022/8/9 00:05:16