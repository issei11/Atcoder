import math
N = int(input())
A = list(map(int,input().split()))
cnt = 0
s = 0
for a in A:
    if a > 0:
        cnt += 1
        s += a

print(math.ceil(s/cnt))
#2022/8/2 00:02:51