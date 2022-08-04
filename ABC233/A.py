x,y = map(int,input().split())

if (y-x) <= 0:
    print(0)
elif (y-x)%10 == 0:
    print((y-x)//10)
else:
    print((y-x)//10+1)
#2022/4/30 00:03:50