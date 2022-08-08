h1,w1 = map(int,input().split())
h2,w2 = map(int,input().split())

if h1 == w2 or h1 == h2 or w1 == w2 or w1 == h2:
    print('YES')
else:
    print('NO')
#2022/8/8 00:02:02