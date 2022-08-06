from itertools import product

N = int(input())
S = ['a','b','c']
ans = ''
for pro in product(range(3),repeat=N):
    for i in range(N):
        ans = ans+S[pro[i]]
    print(ans)
    ans = ''
#2022/8/6 00:06:21