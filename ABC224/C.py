N = int(input())
X,Y = [0],[0]
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

cnt = N*(N-1)*(N-2)//6
for i in range(1,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N+1):
            if (Y[j]-Y[i])*(X[k]-X[i]) == (Y[k]-Y[i])*(X[j]-X[i]):
                cnt -= 1
print(cnt)

#2022/5/7 00:12:56