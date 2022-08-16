K = int(input())
h = 21
m = 0
m += K%60
h += K//60
mm = str(m).zfill(2)
hh = str(h)
print(hh+':'+mm)