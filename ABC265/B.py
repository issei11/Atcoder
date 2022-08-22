N,M,T = map(int,input().split())
A = list(map(int,input().split()))
time = T
i = 0
for _ in range(M):
    x,y = map(int,input().split())
    x -= 1
    while i < x:
        time -= A[i]
        i += 1
    if time <= 0:
        print('No')
        exit()
    time += y
while i < N-1:
    time -= A[i]
    i += 1
if time <= 0:
    print('No')
else:
    print('Yes')