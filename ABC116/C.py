N = int(input())
h = list(map(int,input().split()))
h_max = max(h)
cnt = 0
for height in range(1,h_max+1):
    for i in range(N-1):
        if h[i] >= height and h[i+1] < height:
            cnt += 1
    if h[N-1] >= height:
        cnt += 1
print(cnt)
#2022/8/5 00:08:32