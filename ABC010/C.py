txa,tya,txb,tyb,T,V = map(int,input().split())
n = int(input())
X,Y = [],[]
for _ in range(n):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

P = 0
Q = 0
R = (T*V)**2
for i in range(n):
    P = (txa-X[i])**2+(tya-Y[i])**2
    Q = (txb-X[i])**2+(tyb-Y[i])**2
    if 4*P*Q <= (R-P-Q)**2:
        print('YES')
        exit()
print('NO')
#2022/8/1 00:14:17