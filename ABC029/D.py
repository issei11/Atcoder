from itertools import product
import sys

def f(n):
    n = str(n)
    digit = len(n)
    n_max = int(n[0])
    n = int(n)
    if digit == 1:
        if n >= 1:
            return 1
        else:
            return 0
    cnt = 0
    for pro in product(range(2),repeat= digit-1):
        s = sum(pro)
        cnt += 9**(digit-1-s)*s
    ans = 0
    for i in range(n_max+1):
        if i == n_max:
            if n_max == 1:
                ans += n-n_max*10**(digit-1) + 1 + f(n-n_max*10**(digit-1))
            else:
                ans += f(n-n_max*10**(digit-1))
        elif i == 1:
            ans += 10**(digit-1) + cnt
        else:
            ans += cnt
    return ans

N = int(input())
print(f(N))
#2022/8/6 00:50:52