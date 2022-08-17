a,b = map(int,input().split())
if a == b:
    print('Draw')
elif 1 < a < b or b == 1:
    print('Bob')
elif a > b > 1 or a == 1:
    print('Alice')
#2022/8/16 00:03:22