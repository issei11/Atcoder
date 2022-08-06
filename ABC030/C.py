N,M = map(int,input().split())
X,Y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

i,j = 0,0
t = 0
place = 'a'
ans = 0
while True:
    if place == 'a':
        if t <= a[i]:
            place = 'b'
            t = a[i]+X
        else:
            i += 1
            if i == N:
                break
    elif place == 'b':
        if t <= b[j]:
            place = 'a'
            t = b[j]+Y
            ans += 1
        else:
            j += 1
            if j == M:
                break
print(ans)