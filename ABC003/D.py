import math

def combinations_count(n, r):#組み合わせの計算, import math を忘れずに
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

R,C = map(int,input().split())
X,Y = map(int,input().split())
D,L = map(int,input().split())
mod = 10**9+7

area_num = (R-X+1)*(C-Y+1)
area = X*Y
comb = combinations_count(area,D)
comb *= combinations_count(area-D,L)
comb2 = 0
comb3 = 0
if D+L <= area-Y:
    comb2 += combinations_count(area-Y,D)*combinations_count(area-Y-D,L)
if D+L <= area-X:
    comb3 += combinations_count(area-X,D)*combinations_count(area-X-D,L)

print((area_num*comb-(area_num+Y)*comb2-(area_num+X)*comb3)%mod)