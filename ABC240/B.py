N = int(input())
a = list(map(int,input().split()))

a = sorted(a)

cnt = 1

for i in range(N-1):
    if a[i+1]-a[i] >= 1:
        cnt += 1

print(cnt)

#2022/4/24 00:05:13