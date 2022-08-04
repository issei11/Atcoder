N = int(input())
a = [0] + list(map(int,input().split()))

ans = 0

cnt = 0
for i in range(1,N+1):
    if a[i] == i:
        cnt += 1
ans += cnt*(cnt-1)//2

cnt = 0
for i in range(1,N+1):
    if a[i] != i:
        if a[a[i]] == i:
            cnt += 1
ans += cnt//2

print(ans)