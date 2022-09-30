x,y,z = map(int,input().split())
if 0 < x < y or y < x < 0 or x < 0 < y or y < 0 < x:
    print(abs(x))
else:
    if 0 < z < y or y < z < 0 or z < 0 < y or y < 0 < z:
        p = z
        print(abs(z)+abs(x-z))
    else:
        print(-1)