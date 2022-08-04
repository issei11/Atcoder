a,b,c = map(int,input().split())

flag = True
for i in range(a,b+1):
    if i%c == 0:
        print(i)
        flag = False
        break

if flag == True:
    print(-1)
#2022/5/9 00:03:47