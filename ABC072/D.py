N = int(input())
p = list(map(int,input().split()))

ans = 0
cnt = 0
i = 0
while i < N:
    if p[i] == i+1:
        cnt = 1
        i += 1
        while i < N and p[i] == i+1:
            i += 1
            cnt += 1
        ans += (cnt+1)//2
        cnt = 0
    else:
        i += 1
print(ans)
#2022/8/26 00:09:08