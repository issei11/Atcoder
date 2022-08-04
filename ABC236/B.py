N = int(input())
A = list(map(int,input().split()))

cnt = [0]*(N+1)
cnt[0] = 4

for i in A:
    cnt[i] += 1

for i in range(N+1):
    if cnt[i] == 3:
        print(i)
#2022/4/27 00:05:19