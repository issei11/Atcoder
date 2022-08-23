X,A,B = map(int,input().split())
if A >= B:
    print('delicious')
elif (A+X) >= B:
    print('safe')
else:
    print('dangerous')
#2022/8/23 00:03:27 1WA