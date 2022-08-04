N,D = map(int,input().split())
X,Y = map(int,input().split())
dist_min = X//D + Y//D
if X%D != 0 or Y%D != 0 or N < dist_min:
    print('NO')
    exit()
X = X//D
Y = Y//D
D = 1
dist_min = X+Y

#2022/8/1 00:21:07