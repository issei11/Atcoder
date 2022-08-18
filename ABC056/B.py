W,a,b = map(int,input().split())
if a+W-b < 0 or b+W-a < 0:
    print(min(abs(a+W-b),abs(b+W-a)))
else:
    print(0)
#2022/8/17 00:05:46