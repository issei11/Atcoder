a,b,c,d = map(int,input().split())
if a*d < b*c:
    print('TAKAHASHI')
elif a*d > b*c:
    print('AOKI')
else:
    print('DRAW')