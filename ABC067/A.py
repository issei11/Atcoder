A,B = map(int,input().split())
a = [A,A+B,B]
for x in a:
    if x%3 == 0:
        print('Possible')
        exit()
print('Impossible')
#2022/8/23 00:02:39