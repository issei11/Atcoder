N = int(input())
ans = hex(N)
if len(ans) == 4:
    print(ans[2:4].upper())
else:
    print('0'+ans[2].upper())
