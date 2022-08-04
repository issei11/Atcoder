N = int(input())
s = set()
ans = 0
for _ in range(N):
    A = int(input())
    if A in s:
        ans += 1
    else:
        s.add(A)
print(ans)
#2022/8/4 00:02:15