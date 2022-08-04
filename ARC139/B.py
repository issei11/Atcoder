import numpy as np

T = int(input())
cost = 0
list = []
for i in range(T):
    n,a,b,x,y,z = (map(int,input().split()))
    list.append([n,a,b,x,y,z])

for i in range(T):
    N = list[i][0]
    A = list[i][1]
    B = list[i][2]
    X = list[i][3]
    Y = list[i][4]
    Z = list[i][5]
    Y = min(Y, A*X)
    Z = min(Z, B*X)
    if Y*B >= Z*A: #V/A>Z/B
        cost += N//B * Z
        N = N-(N//B)*B
        cost += N*X
    else:
        cost += N//A * Y
        N = N-(N//A)*A
        cost += N*X
    print(cost)
    cost = 0