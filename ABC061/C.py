arr = [0 for _ in range(10**5+1)]
N,K = map(int,input().split())
for _ in range(N):
    a,b = map(int,input().split())
    arr[a] += b
cnt = 0
i = 1
while cnt < K:
    cnt += arr[i]
    i += 1
print(i-1)
#2022/8/21 00:04:47