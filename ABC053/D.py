N = int(input())
A = list(map(int,input().split()))

d = dict()
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

mod2_0 = 0
mod2_1 = 0
for key in d.keys():
    if d[key]%2 == 0:
        mod2_0 += 1
    else:
        mod2_1 += 1
ans = (mod2_0//2)*2 + mod2_1
print(ans)
#2022/8/15 00:13:00