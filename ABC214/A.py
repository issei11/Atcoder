N = int(input())
ans = 0
if N < 126:
    ans = 4
elif N < 212:
    ans = 6
else:
    ans = 8
print(ans)