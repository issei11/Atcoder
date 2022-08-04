Y = int(input())
ans = 0
if Y%4 == 0:
    ans = Y+2
elif Y%4 == 1:
    ans = Y+1
elif Y%4 == 2:
    ans = Y
else:
    ans = Y+3
print(ans)