a,b,c,d = map(int,input().split())
L = a+b
R = c+d
if L > R:
    print('Left')
elif L == R:
    print('Balanced')
else:
    print('Right')
#2022/8/30 00:01:43