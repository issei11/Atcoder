x1,y1,x2,y2 = map(int,input().split())

list1 = [[x1+1,y1+2],[x1+2,y1+1],[x1-1,y1+2],[x1+2,y1-1],[x1-2,y1+1],[x1+1,y1-2],[x1-1,y1-2],[x1-2,y1-1]]
list2 = [[x2+1,y2+2],[x2+2,y2+1],[x2-1,y2+2],[x2+2,y2-1],[x2-2,y2+1],[x2+1,y2-2],[x2-1,y2-2],[x2-2,y2-1]]

flag =False

for i in range(8):
    for j in range(8):
        if list1[i] == list2[j]:
            flag = True

if flag:
    print('Yes')
else:
    print('No')

#2022/4/25 00:15:44