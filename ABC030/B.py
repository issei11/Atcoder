n,m = map(int,input().split())
n = n%12
long_deg = m*6
short_deg = n*30+m/2
if long_deg > short_deg:
    print(long_deg-short_deg if long_deg-short_deg <= 180 else 360-(long_deg-short_deg))
else:
    print(short_deg-long_deg if short_deg-long_deg <= 180 else 360-(short_deg-long_deg))