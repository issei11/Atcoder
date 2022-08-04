import math
def comb(n,r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
L = int(input())
print(comb(L-1,11))
#2022/6/9 00:06:19