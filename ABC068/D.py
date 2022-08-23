K = int(input())
N = 50
a = [49 for _ in range(N)]
k = K//50
r = K%50
if r != 0:
    for i in range(N-r):
        a[i] = k+(N-r)-1
    for i in range(N-r,N):
        a[i] = a[0]+N+1
else:
    for i in range(N):
        a[i] += k
print(N)
print(*a)
#2022/8/24 00:17:32