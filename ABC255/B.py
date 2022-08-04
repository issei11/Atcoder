N,K = map(int,input().split())
A = list(map(int,input().split()))
A = set(A)
light_X = []
not_light_X = []
light_Y = []
not_light_Y = []
for i in range(1,N+1):
    x,y = map(int,input().split())
    if i in A:
        light_X.append(x)
        light_Y.append(y)
    else:
        not_light_X.append(x)
        not_light_Y.append(y)


tmp = 0
min = [10**11+7 for i in range(len(not_light_X))]
for i in range(len(not_light_X)):
    for j in range(len(light_X)):
        tmp = (light_X[j]-not_light_X[i])**2+(light_Y[j]-not_light_Y[i])**2
        if min[i] > tmp:
            min[i] = tmp
print((max(min))**0.5)