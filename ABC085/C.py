N,Y = map(int,input().split())
Y //= 1000

tmp = 0
for i in range(N+1):
    for j in range(N+1):
        tmp = i*10+j*5
        if Y-tmp == N-i-j and N-i-j >= 0:
            print(i,j,N-i-j)
            exit()
print(-1,-1,-1)
#2022/8/30 00:08:00