x,y = map(int,input().split())
group_1 = [1,3,5,7,8,10,12]
group_2 = [4,6,9,11]

if (x in group_1 and y in group_1) or (x in group_2 and y in group_2):
    print('Yes')
else:
    print('No')
#2022/8/22 00:03:20