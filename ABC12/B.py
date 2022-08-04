N = int(input())
h = N//3600
m = (N//60)-h*60
s = N%60
if h < 10:
    h = [0,h]
else:
    h = [h//10,h%10]
if m < 10:
    m = [0,m]
else:
    m = [m//10,m%10]
if s < 10:
    s = [0,s]
else:
    s = [s//10,s%10]
print(h[0],h[1],':',m[0],m[1],':',s[0],s[1],sep='')

#2022/7/22 00:06:26