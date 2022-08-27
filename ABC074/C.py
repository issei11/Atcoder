a,b,c,d,e,f = map(int,input().split())

dp = [[[[0 for _ in range(31)] for _ in range(31)] for _ in range(31)] for _ in range(31)]

ans_sugar_water = 10**9+7
ans_suger = 1
for A in range(31):
    for B in range(31-A):
        for C in range(31):
            for D in range(31):
                tmp_sugar_water = 100*(a*A+b*B)+(c*C+d*D)
                tmp_sugar = c*C+d*D
                if tmp_sugar_water <= f:
                    if (100+e)*tmp_sugar <= e*tmp_sugar_water and ans_sugar_water*tmp_sugar > ans_suger*tmp_sugar_water:
                        ans_sugar_water = tmp_sugar_water
                        ans_suger = tmp_sugar
ans_0 = [100*a,0]
if ans_sugar_water != 10**9+7 and ans_suger != 1:
    print(ans_sugar_water,ans_suger)
else:
    print(100*a,0)
#2022/8/26 00:33:05