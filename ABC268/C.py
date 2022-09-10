N = int(input())
p = list(map(int,input().split()))

cnt = [0 for _ in range(N)]

for i in range(N):
    cnt[(p[i]-i-1)%N] += 1
    cnt[(p[i]-i)%N] += 1
    cnt[(p[i]-i+1)%N] += 1
print(max(cnt))