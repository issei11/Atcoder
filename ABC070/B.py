a,b,c,d = map(int,input().split())
if b <= c or d <= a:
    print(0)
else:
    if b < d:
        if a < c:
            print(b-c)
        else:
            print(b-a)
    else:
        if a < c:
            print(d-c)
        else:
            print(d-a)
#2022/8/25 00:06:31 1WA