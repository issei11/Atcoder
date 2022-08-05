N,A,B = map(int,input().split())
x = 0
for _ in range(N):
    s,d = input().split()
    d = int(d)
    if s == 'East':
        if d < A:
            x += A
        elif d > B:
            x += B
        else:
            x += d
    if s == 'West':
        if d < A:
            x -= A
        elif d > B:
            x -= B
        else:
            x -= d

if x > 0:
    print('East',x)
elif x < 0:
    print('West',-x)
else:
    print(0)
#2022/8/5 00:09:47