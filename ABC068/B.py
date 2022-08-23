N = int(input())
ans = 1
ans_score = 0
for i in range(2,N+1):
    n = i
    tmp = 0
    while n%2 == 0 and n != 0:
        n = n//2
        tmp += 1
    if ans_score < tmp:
        ans_score = tmp
        ans = i
print(ans)
#2022/8/24 00:06:51 3WA