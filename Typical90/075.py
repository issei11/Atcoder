N = int(input())

cnt = 0
i = 2
n = N
while i*i <= N:
    while n%i == 0:
        cnt += 1
        n = n//i
    i += 1
if n != 1:
    cnt += 1

ans = 0
j = 1
while cnt > j:
    ans += 1
    j *= 2
print(ans)
