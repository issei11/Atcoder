N = int(input())
a = list(map(int,input().split()))
a = sorted(a,reverse=True)
A = set()
cnt = 0
for x in a:
    if not(x in A):
        cnt += 1
    while x > 0:
        A.add(x)
        if x%2 == 0:
            x = x//2
        else:
            break
print(cnt)

#2022/8/4 00:17:29 1WA