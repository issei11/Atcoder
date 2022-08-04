L,R = map(int,input().split())
min = 10**9
if R-L >= 2019:
    print(0)
else:
    for i in range(L,R):
        for j in range(i+1,R+1):
            mod = (i*j)%2019
            if min > mod:
                min = mod
    print(min)
#2022/7/15 00:07:12