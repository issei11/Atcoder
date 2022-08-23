N = int(input())
a = [int(input()) for _ in range(N)]

now = 1
for i in range(N):
    now = a[now-1]
    if now == 2:
        print(i+1)
        exit()
print(-1)

#2022/8/23 00:03:36