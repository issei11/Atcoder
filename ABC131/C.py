import math

a,b,c,d = map(int,input().split())
x = b-a+1
y = b//c-(a-1)//c
z = b//d-(a-1)//d
l = c*d//math.gcd(c,d)
w = b//l-(a-1)//l
print(x-y-z+w)
print(x,y,z,l,w)

#2022/7/15 00:34:40